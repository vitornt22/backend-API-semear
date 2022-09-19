from church.models import Church
from django.db import models
from informations.models import Adress


# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    personResponsible = models.CharField(
        max_length=80, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    id_adress = models.IntegerField(blank=True, null=True)
