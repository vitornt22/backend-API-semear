from django.contrib import admin

# Register your models here.
from .models import Information, UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    ...
