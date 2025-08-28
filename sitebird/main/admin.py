from django.contrib import admin
from .models import Bird, Categories


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'category', 'in_the_red_book')
    list_display_links = ('id', 'title')
    ordering = ['id']
    list_editable = ['is_published']
    list_per_page = 10


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    list_per_page = 10
