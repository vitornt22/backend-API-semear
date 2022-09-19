from django.db import models
from user.models import UserModel


# Create your models here.
class Donor(models.Model):
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=80, null=False, blank=False)
