from church.models import Church
from django.db import models
from informations.models import Adress
from user.models import Information, UserModel


# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    id_church = models.IntegerField()
    id_adress = models.IntegerField(null=False)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    information = models.ForeignKey(
        Information, on_delete=models.CASCADE, null=True, blank=True)


class Follower(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, null=True)
    user2 = models.ForeignKey(
        UserModel, related_name='user2', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
