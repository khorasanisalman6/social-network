from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics/')
    bio = models.TextField(blank=True)
    age = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)