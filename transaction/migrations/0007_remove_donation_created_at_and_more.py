# Generated by Django 4.1.1 on 2022-10-26 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_donation_created_at_donation_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='updated_at',
        ),
    ]
