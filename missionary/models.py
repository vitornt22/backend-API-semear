from church.models import Church
from django.db import models
from user.models import UserModel


# Create your models here.
class Missionary(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    ministery = models.CharField(max_length=14, null=False, blank=False)
    fullName = models.CharField(max_length=80, null=False, blank=False)
