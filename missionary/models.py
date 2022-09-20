from church.models import Church
from django.db import models
from informations.models import Adress
from user.models import UserModel


# Create your models here.
class Missionary(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    fullName = models.CharField(max_length=80, null=False, blank=False)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
