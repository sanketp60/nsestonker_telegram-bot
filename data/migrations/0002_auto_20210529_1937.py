# Generated by Django 3.2.3 on 2021-05-29 19:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ClientID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StocksList',
            fields=[
                ('StocksListID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Symbol', models.CharField(max_length=30)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
