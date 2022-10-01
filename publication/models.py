
from django.db import models
from project.models import Project
from user.models import UserModel


# Create your models here.
# Create your models here.j
class Publication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    id_user = models.IntegerField()
    likes = models.ManyToManyField(
        UserModel, related_name='likes', through="Like")
    comments = models.ManyToManyField(
        UserModel, related_name='comments', through="Comment")
    upload = models.ImageField(blank=True, null=True, upload_to='media/')
    legend = models.CharField(max_length=600, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_accountability = models.BooleanField(default=False)


class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, null=False)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, null=False)
    comment = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
