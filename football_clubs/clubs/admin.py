from django.contrib import admin

from .models import Clubs, Countries, Articles


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'town', 'country', 'emblem')
    search_fields = ['name', 'town', 'country']


@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'club', 'title', 'author', 'time_create', 'time_update')
    search_fields = ['club', 'author', 'time_create', 'time_update']
