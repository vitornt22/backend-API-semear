from django.contrib import admin

# Register your models here.
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    ...
