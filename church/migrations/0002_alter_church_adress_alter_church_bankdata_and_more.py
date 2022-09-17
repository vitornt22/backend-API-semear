# Generated by Django 4.1.1 on 2022-09-17 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0001_initial'),
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='adress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informations.adress'),
        ),
        migrations.AlterField(
            model_name='church',
            name='bankData',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informations.bankdata'),
        ),
        migrations.AlterField(
            model_name='church',
            name='pix',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informations.pix'),
        ),
    ]
