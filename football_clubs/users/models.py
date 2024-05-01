from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Users(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name="Фото профілю")
