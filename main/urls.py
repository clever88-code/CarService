from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    
    
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("registration/", views.Register.as_view(), name="registration"),
]


