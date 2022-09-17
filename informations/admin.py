from django.contrib import admin

from .models import PIX, Adress, BankData

# Register your models here.


@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    ...


@admin.register(BankData)
class BankDataAdmin(admin.ModelAdmin):
    ...


@admin.register(PIX)
class PIXAdmin(admin.ModelAdmin):
    ...
