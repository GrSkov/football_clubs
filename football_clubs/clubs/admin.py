from django.contrib import admin

from .models import Clubs, Countries, Articles


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'town', 'country', 'emblem')
    search_fields = ['name', 'town', 'country']
    list_display_links = ('name',)


@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'club', 'country', 'author', 'time_create', 'time_update')
    list_display_links = ('title',)
    search_fields = ['club', 'author', 'time_create', 'time_update']
    ordering = ['-time_create']
    list_editable = ('club',)
    list_per_page = 5
