from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    class AccountCategory(models.TextChoices):
        CLIENT = "CL", _("Client")
        EMPLOYEE = "EM", _("Employee")
        SUPPLIER = "SP", _("Supplier")

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=AccountCategory.choices)
    balance = models.FloatField()
    last_transaction = models.DateField(default=timezone.now)
    is_active = models.BooleanField()

    def get_category_display(self):
        return dict(self.AccountCategory.choices)[self.category]


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        PAYMENT = "PY", _("Payment (Supplier) +")
        RECEIVABLE = "RV", _("Receivable (Supplier) -")
        DEBT = "DB", _("Debt (Client) +")
        COLLECTION = "CL", _("Collection (Client) -")

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    account_after = models.FloatField()

    def get_type_display(self):
        return dict(self.TransactionType.choices)[self.type]

