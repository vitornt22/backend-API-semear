from django.db import models


# Create your models here.
class Donor(models.Model):
    fullName = models.CharField(max_length=80, null=False, blank=False)
