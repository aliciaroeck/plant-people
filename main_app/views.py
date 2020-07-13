from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# models
from .models import Profile
# forms
from .forms import Create_Profile_Form
# Create your views here.


# Home/login Route
def landing(request):
    form = Create_Profile_Form()
    error_message = ''
    if request.method == 'POST':
        form = Create_Profile_Form(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(email = request.POST['email'], location = request.POST['location'], full_name= request.POST['full_name'], user = user)
            login(request,user)
            return redirect('community')
        else:
            error_message = 'Invalid form'

    context = {'form':form, 'error_message': error_message}
    return render(request, 'landing.html', context)

# Login Route
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return render(request,'landing.html',{'error':'Invalid Username or Password'})


# Community Posts Route
def community(request):
    return render(request, 'community/index.html')

# Personal Profile Route
def profile(request):
    return render(request, 'registration/profile.html')


