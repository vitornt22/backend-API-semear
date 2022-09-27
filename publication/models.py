from django.db import models
from user.models import UserModel


# Create your models here.
class Publication(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    id_user = models.IntegerField()

    upload = models.ImageField(blank=True, null=True, upload_to='uploads/')
    legend = models.CharField(max_length=600, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_accountability = models.BooleanField(default=False)
