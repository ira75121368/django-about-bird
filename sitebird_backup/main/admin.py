from django.contrib import admin
from .models import Bird, Categories


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'category', 'in_the_red_book')
    list_display_links = ('id', 'title')
    ordering = ['id']
    list_editable = ['is_published']
    list_per_page = 10
    actions = ['blok_published', 'blok_unpublished']
    search_fields = ['title__startswith']
    list_filter = ['category__name', 'is_published', 'in_the_red_book']

    @admin.action(description='Сделать записи опубликованными')
    def blok_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Опубликовано {count} записей')

    @admin.action(description='Снять записи с публикации')
    def blok_unpublished(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Снято с публикации {count} записей')



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    list_per_page = 10
