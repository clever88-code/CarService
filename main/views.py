from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

# Create your views here.



def index(request):
    return render(request, 'main/index.html' )

def login(request):
    return render(request, 'main/login.html' )



class Register(CreateView):
    form_class = RegisterUserForms
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"


class LoginUser(LoginView):
    form_class = LoginUserForms
    template_name = 'registration/login.html'