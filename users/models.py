from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(default='google.jpg', upload_to = 'profile_pictures')
    gender = models.CharField(max_length=6, null=True)
    email = models.EmailField(default='dj@dj.com')
    worked_for = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    water = models.CharField(max_length=50, blank=True, null=True)
    lunch = models.CharField(max_length=50, blank=True, null=True)
    dinner = models.CharField(max_length=50, blank=True, null=True)
    brakefast = models.CharField(max_length=50, blank=True, null=True)
    refreshment = models.CharField(max_length=50, blank=True, null=True)
    block = models.CharField(max_length=50, blank=True, null=True)
    dorm = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.first_name