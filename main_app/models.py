from django.db import models
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    email       = models.EmailField(max_length=50, unique=True)
    location    = models.CharField(max_length=50)
    full_name   = models.CharField(max_length=50)
    bio         = models.TextField(max_length=1000, blank=True)
    date_joined = models.DateField(default=timezone.now)
    image       = models.ImageField(default='images/avatar.jpg', upload_to='images/profile_pics')


    def __str__(self):
        return self.full_name