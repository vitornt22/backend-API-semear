
from django.db import models


# Create your models here.
class Pix(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryKey = models.CharField(max_length=20, blank=False, null=False)
    key = models.CharField(max_length=32, blank=False, null=False)


class BankData(models.Model):
    holder = models.CharField(max_length=50, blank=False, null=False)
    cnpj = models.CharField(max_length=18, blank=False, null=False)
    bank = models.CharField(max_length=12, blank=False, null=False)
    agency = models.CharField(max_length=5, blank=False, null=False)
    # OBS: ANALISAR API PARA CHECAR TIPO DE CAMPO
    agencyDigit = models.IntegerField(blank=False, null=False)
    account = models.CharField(max_length=20, blank=False, null=False)
    accountDigit = models.IntegerField(blank=False, null=False)
    accountType = models.CharField(max_length=20, blank=True, null=True)
