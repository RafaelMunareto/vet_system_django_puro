from django.urls import path
from .views import *

urlpatterns = [
    
    path('login/cadastro', users.cadastro, name='login.cadastro'),
    path('login', users.login, name='login'),
    path('logout', users.logout, name='logout'),
   
]
