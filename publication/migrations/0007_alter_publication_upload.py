# Generated by Django 4.1.1 on 2022-10-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0006_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
