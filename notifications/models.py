
from django.db import models
from publication.models import Publication
from user.models import UserModel


# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(
        UserModel, related_name='sender', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(
        UserModel, related_name='receiver', on_delete=models.CASCADE, null=True)  # noqa
    is_anonymous = models.BooleanField(default=False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    seen = models.BooleanField(default=False)
