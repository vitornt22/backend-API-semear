from django.contrib import admin

# Register your models here.
from .models import Comment, Like, Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    ...


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
