from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    balance = models.FloatField()
    last_transaction = models.DateField()
    is_active = models.BooleanField()


class Transaction(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    account_after = models.FloatField()

