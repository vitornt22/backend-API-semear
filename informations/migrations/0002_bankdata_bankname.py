# Generated by Django 4.1.1 on 2022-10-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdata',
            name='bankName',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
