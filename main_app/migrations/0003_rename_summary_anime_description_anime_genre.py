# Generated by Django 4.0.2 on 2022-02-17 03:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_anime_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='summary',
            new_name='description',
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=[], size=None),
        ),
    ]
