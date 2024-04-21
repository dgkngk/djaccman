from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from djaccman_app.models import Account, Transaction
from djaccman_app.forms import AccountForm, TransactionForm


def login_view(request):
    # View for user login page
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome to Account Management App, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    # View for user logout
    logout(request)
    return redirect('login')


@login_required(redirect_field_name='next', login_url='login')
def home_view(request):
    accounts = Account.objects.all().exclude(is_active=False)
    return render(request, 'home.html',
                  {'accounts': accounts,
                   'form': AccountForm})


@login_required(redirect_field_name='next', login_url='login')
def details_view(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    transactions = Transaction.objects.filter(account_id=account_id)
    return render(request, 'details.html',
                  {'account': account, 'transactions': transactions, 'form': TransactionForm})


@login_required(redirect_field_name='next', login_url='login')
def create_transaction_view(request, account_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            account = Account.objects.get(pk=account_id)
            form.instance.account_id = account

            transaction_date = form.instance.date
            transaction_type = form.instance.type
            if (transaction_type == Transaction.TransactionType.PAYMENT
                    or transaction_type == Transaction.TransactionType.DEBT):
                account.balance += form.instance.amount
            else:
                account.balance -= form.instance.amount
            form.instance.account_after = account.balance
            account.last_transaction = transaction_date
            account.save()
            form.save()
            messages.success(request, 'Transaction created successfully')
    else:
        form = TransactionForm()
        messages.error(request, 'Invalid request')
    return redirect('details', account_id=account_id)


@login_required(redirect_field_name='next', login_url='login')
def create_account_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.instance.is_active = True
            form.save()
            messages.success(request, 'Account created successfully')
    else:
        form = AccountForm()
        messages.error(request, 'Invalid request')
    return redirect('home')
