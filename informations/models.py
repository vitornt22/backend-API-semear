from django.db import models

# Create your models here.


class Adress(models.Model):
    zip_code = models.CharField(max_length=9, null=False, blank=False)
    adress = models.CharField(max_length=80, null=True, blank=True)
    number = models.CharField(max_length=9, null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    district = models.CharField(max_length=80, null=True, blank=True)


class BankData(models.Model):
    holder = models.CharField(max_length=80, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    bank = models.CharField(max_length=8, null=False, blank=False)
    agency = models.CharField(max_length=5, null=False, blank=False)
    digitAgency = models.CharField(max_length=1, null=False, blank=False)
    account = models.CharField(max_length=20, null=False, blank=False)
    digitAccount = models.CharField(max_length=1, null=False, blank=False)


class PIX (models.Model):
    typeKey = models.CharField(max_length=10, null=False, blank=False)
    valueKey = models.CharField(max_length=100, null=False, blank=False)
