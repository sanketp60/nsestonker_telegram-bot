import sys
import uuid

try:
    from django.db import models
except  Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

class Client(models.Model):
    ClientID = models.CharField(max_length=20, primary_key=True)
    ClientName = models.CharField(max_length=128)
    def __str__(self):
        return self.ClientName

class StocksList(models.Model):
    StocksListID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Symbol = models.CharField(max_length=30)