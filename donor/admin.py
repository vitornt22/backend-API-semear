from django.contrib import admin

# Register your models here.
from .models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    ...
