from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Clubs(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва команди')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, blank=True, verbose_name='Slug')
    emblem = models.ImageField(upload_to='media/photos/', verbose_name='Емблема команди')
    town = models.CharField(max_length=50, verbose_name='Місто')
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, max_length=30, verbose_name='Країна')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.name, 'uk', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команди'
        verbose_name_plural = 'Команди'


class Countries(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Назва країни')
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name='Slug')
    flag = models.ImageField(upload_to='media/photos/', verbose_name='Прапор країни')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.name, 'uk', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Країни'
        verbose_name_plural = 'Країни'


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва статті')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Стаття')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час редагування')
    club = models.ForeignKey('Clubs', on_delete=models.CASCADE, null=True, verbose_name='Команда')
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, null=True, verbose_name='Країна')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    photo = models.ImageField(upload_to='media/photos/', blank=True, verbose_name='Зображення')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.title, 'uk', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статті'
        verbose_name_plural = 'Статті'

    def get_absolute_url(self):
        return reverse('show_article', kwargs={'article_slug': self.slug})
