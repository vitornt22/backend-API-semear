# Generated by Django 4.1.1 on 2022-09-17 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personResponsible', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=50)),
                ('church', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='church.church')),
            ],
        ),
    ]
