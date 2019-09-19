""" Profile class created in order to add user and image for a profile account """
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """"pip install pillow to get ImageField, image set by default when profile is created"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
