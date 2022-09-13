from django.db import models
from user.models import UserModel

# Create your models here.


class Church (UserModel):
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    ministery = models.CharField(max_length=14, null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False)
    contact = models.CharField(max_length=15, null=False, blank=False)
