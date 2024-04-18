from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    balance = models.IntegerField(default=0)
    last_transaction = models.DateField()


class Transaction(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    account_after = models.IntegerField()

