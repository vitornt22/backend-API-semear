from django.contrib import admin

# Register your models here.
from .models import Church


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    ...
