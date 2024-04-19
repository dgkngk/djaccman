from django.urls import path, include
from .views import (login_view, logout_view, home_view, details_view)


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
    path('details/<int:account_id>/', details_view, name='details'),
]
