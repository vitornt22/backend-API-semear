from django.contrib import admin

# Register your models here.
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    ...
