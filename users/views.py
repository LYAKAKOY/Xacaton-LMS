from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterUserForm


# Create your views here.
class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
