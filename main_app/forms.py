from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from .models import User

class Create_Profile_Form(UserCreationForm):
    full_name   = forms.CharField(max_length=50)
    location    = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username','full_name', 'email', 'location']