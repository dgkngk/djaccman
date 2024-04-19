from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from djaccman_app.models import Account, Transaction


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
    return render(request, 'home.html', {'accounts': accounts})


def details_view(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    transactions = Transaction.objects.filter(account_id=account_id)
    return render(request, 'details.html', {'account': account, 'transactions': transactions})