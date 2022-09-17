# Generated by Django 4.1.1 on 2022-09-17 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministery', models.CharField(max_length=14)),
                ('fullName', models.CharField(max_length=80)),
                ('church', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='church.church')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
