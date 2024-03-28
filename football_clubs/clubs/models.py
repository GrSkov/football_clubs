from django.db import models


class Clubs(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва команди')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='Slug')
    emblem = models.ImageField(upload_to='photos/', verbose_name='Емблема команди')
    town = models.CharField(max_length=50, verbose_name='Місто')
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, max_length=30, verbose_name='Країна')
    article = models.CharField(max_length=255, blank=True, verbose_name='Назва статті')
    content = models.TextField(verbose_name='Стаття')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час редагування')


class Countries(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Назва країни')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')
    flag = models.ImageField(upload_to='photos/', verbose_name='Прапор країни')
