from django.contrib import admin

from .models import Follower, Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    ...
