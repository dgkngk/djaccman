from django.forms import ModelForm

from .models import Account, Transaction


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'category', 'balance']


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount', 'date', 'description', 'type']
