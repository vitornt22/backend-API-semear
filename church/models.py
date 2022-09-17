from django.db import models
from informations.models import PIX, Adress, BankData
from user.models import UserModel

# Create your models here.


class Church (models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    ministery = models.CharField(max_length=14, null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE)
    bankData = models.OneToOneField(BankData, on_delete=models.CASCADE)
    pix = models.OneToOneField(PIX, on_delete=models.CASCADE)
