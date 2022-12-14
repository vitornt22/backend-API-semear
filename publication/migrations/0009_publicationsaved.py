# Generated by Django 4.1.1 on 2022-10-10 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0008_remove_publication_project_publication_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationSaved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publication.publication')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
