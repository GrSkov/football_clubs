from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Clubs, Countries, Articles


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'town', 'country', 'emblem_photo')
    search_fields = ['name', 'town', 'country']
    list_display_links = ('name',)

    @admin.display(description='Емблема', ordering='content')
    def emblem_photo(self, club: Clubs):
        if club.emblem:
            return mark_safe(f"<img src='{club.emblem.url}' width='10%'>")
        return "Емблема відсутня"


@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country_flag')
    list_display_links = ('name',)

    @admin.display(description='Прапор', ordering='content')
    def country_flag(self, country: Countries):
        if country.flag:
            return mark_safe(f"<img src='{country.flag.url}' width='5%'>")
        return "Прапор відсутній"


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'club', 'country', 'author', 'time_create', 'time_update', 'article_photo')
    list_display_links = ('title',)
    readonly_fields = ['article_photo']
    search_fields = ['club', 'author', 'time_create', 'time_update']
    ordering = ['-time_create']
    list_editable = ('club',)
    list_per_page = 5
    save_on_top = True

    @admin.display(description='Світлина', ordering='content')
    def article_photo(self, article: Articles):
        if article.photo:
            return mark_safe(f"<img src='{article.photo.url}' width='30%'>")
        return "Світлина відсутня"
