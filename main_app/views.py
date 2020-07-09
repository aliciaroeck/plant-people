from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Route
def landing(request):
    return HttpResponse('<h1>Landing Page</h1>')

# Community Posts Route
def community(request):
    return HttpResponse('<h1>Community Posts Page</h1>')

# Personal Profile Route
def profile(request):
    return HttpResponse('<h1>Profile Page</h1>')