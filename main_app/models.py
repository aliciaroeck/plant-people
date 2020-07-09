from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(default='images/avatar.jpg', upload_to='images/profile_pics')
    date_joined = models.DateField(default=timezone.now)
    