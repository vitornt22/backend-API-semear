# Generated by Django 4.1.1 on 2022-10-21 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_information_user'),
        ('missionary', '0011_alter_missionary_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionary',
            name='information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.information'),
        ),
    ]
