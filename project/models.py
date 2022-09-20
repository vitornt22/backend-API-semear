from church.models import Church
from django.db import models
from informations.models import Adress


# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    id_church = models.IntegerField()
    id_adress = models.IntegerField(null=False)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, null=False, blank=False)
