from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']


# Register your models here.
