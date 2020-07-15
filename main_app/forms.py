from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from .models import User, Profile, Post

class Create_Profile_Form(UserCreationForm):
    full_name   = forms.CharField(max_length=50)
    location    = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username','full_name', 'email', 'location']

class EditProfileForm(forms.ModelForm):
    full_name   = forms.CharField(max_length=50)
    location    = forms.CharField(max_length=50)
    bio         = models.TextField(max_length=1000, blank=True)
    class Meta:
        model = Profile
        fields = ('full_name', 'location', 'bio')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class NewContentPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class EditContentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')