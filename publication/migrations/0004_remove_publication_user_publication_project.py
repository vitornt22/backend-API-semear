# Generated by Django 4.1.1 on 2022-09-28 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_follower_project_followers'),
        ('publication', '0003_like_publication_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='user',
        ),
        migrations.AddField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
