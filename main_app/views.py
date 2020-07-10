from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# models

# forms


# Create your views here.


# Home/login Route
def landing(request):
    return render(request, 'landing.html')



# Community Posts Route
def community(request):
    return HttpResponse('<h1>Community Posts Page</h1>')

# Personal Profile Route
def profile(request):
    return HttpResponse('<h1>Profile Page</h1>')


