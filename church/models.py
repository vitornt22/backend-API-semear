from django.db import models
from informations.models import PIX, Adress, BankData
from user.models import Information, UserModel

# Create your models here.


class Church (models.Model):
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=False,
                            blank=False, unique=True)
    ministery = models.CharField(max_length=14, null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False)
    adress = models.ForeignKey(
        Adress, on_delete=models.CASCADE, null=True, blank=True)
    bankData = models.OneToOneField(
        BankData, on_delete=models.CASCADE, null=True, blank=True)
    pix = models.OneToOneField(
        PIX, on_delete=models.CASCADE, null=True, blank=True)

    information = models.ForeignKey(
        Information, on_delete=models.CASCADE, null=True, blank=True)
