from django.contrib import admin

# Register your models here.
from .models import Information, UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        a = self.get_object(request=request, object_id=obj.id)
        if obj.password != a.password:
            obj.set_password(obj.password)
        return super().save_model(request, obj, form, change)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    ...
