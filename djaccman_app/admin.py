from django.contrib import admin
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'balance', 'last_transaction', 'is_active')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'amount', 'date', 'description', 'type', 'account_after')


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction)
