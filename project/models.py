from church.models import Church
from django.db import models


# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    personResponsible = models.CharField(
        max_length=80, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
