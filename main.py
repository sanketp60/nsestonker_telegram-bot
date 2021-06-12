# Django specific settings
import os
import environ

from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.ext import Updater
import logging
from nsetools import Nse
from pprint import pprint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

nse = Nse()

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from data.models import *

def addsymbol(clientid, clientname, symbol):
    try:
        q = nse.get_quote(symbol)
        try:
            client = Client.objects.create(ClientID = str(clientid), ClientName = clientname)
            client.save()
        except:
            client = Client.objects.get(ClientID = str(clientid))
        if StocksList.objects.filter(Client = str(clientid), Symbol = symbol).count():
            output = "Symbol already exists in your list!"
        else:
            stockslistitem = StocksList.objects.create(Client = client, Symbol = symbol)
            stockslistitem.save()
            output = "Symbol added to your list!"
    except:
        output = "Symbol is invalid!"
    return output

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=env('TELEGRAM_TOKEN'), use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot by @sanketp60, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def addtolist(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=addsymbol(update.message.chat['id'], update.message.chat['title'], update.message.text.split(' ')[1]))

addtolist_handler = CommandHandler('addtolist', addtolist)
dispatcher.add_handler(addtolist_handler)

def getstockdetails(update, context):
    try:
        q = nse.get_quote(context.args[0])
        data ='''
Company Name: {companyname}
Symbol: {symbol}
LTP: {ltp}
Open: {open}
High: {high}
Low: {low}
Close: {close}
Prev. Close: {prevclose}
Lower circuit: {lowercircuit}
Upper circuit: {uppercircuit}
        '''.format(
            companyname = q["companyName"],
            symbol = q["symbol"],
            ltp = q["lastPrice"],
            lowercircuit = q["pricebandlower"],
            uppercircuit = q["pricebandupper"],
            open = q["open"],
            high = q["dayHigh"],
            low = q["dayLow"],
            close = q["closePrice"],
            prevclose = q["previousClose"]
            )
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(data)[1:-1])
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid NSE Stock Symbol")

getstockdetails_handler = CommandHandler('getstockdetails', getstockdetails)
dispatcher.add_handler(getstockdetails_handler)

updater.start_polling()