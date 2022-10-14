
from email.policy import default

from django.db import models
from user.models import UserModel


# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey(
        UserModel, related_name='user', on_delete=models.CASCADE, null=True)
    donor = models.ForeignKey(
        UserModel, related_name='donor_field', on_delete=models.CASCADE, null=True)  # noqa
    is_anonymous = models.BooleanField(default=False)
    value = models.FloatField()
    payment_form = models.CharField(max_length=20)
    valid = models.BooleanField(default=False)
    voucher = models.ImageField(blank=True, null=True, upload_to='media/')
