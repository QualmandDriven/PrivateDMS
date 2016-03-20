# Create your models here.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


class DmsUser(models.Model):
    user = models.OneToOneField(User)
