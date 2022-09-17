from django.contrib import admin

from .models import Missionary


# Register your models here.
@admin.register(Missionary)
class MissionaryAdmin(admin.ModelAdmin):
    ...
