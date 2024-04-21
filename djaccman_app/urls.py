from django.urls import path
from .views import (login_view, logout_view, home_view, details_view,
                    create_account_view, create_transaction_view)


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
    path('details/<int:account_id>/', details_view, name='details'),
    path('create_account/', create_account_view, name='create_account'),
    path('create_transaction/<int:account_id>/', create_transaction_view, name='create_transaction'),
]
