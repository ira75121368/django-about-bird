from django.db import models
from django.urls import reverse


# Create your models here.

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Bird(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)
    in_the_red_book = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Categories(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})