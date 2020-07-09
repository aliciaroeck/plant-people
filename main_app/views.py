from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Route
def landing(request):
    return render(request, 'landing.html')

# Community Posts Route
def community(request):
    return HttpResponse('<h1>Community Posts Page</h1>')

# Personal Profile Route
def profile(request):
    return HttpResponse('<h1>Profile Page</h1>')