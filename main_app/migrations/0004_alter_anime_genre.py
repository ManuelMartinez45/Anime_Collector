# Generated by Django 4.0.2 on 2022-02-17 03:26

import django.contrib.postgres.fields
from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_summary_anime_description_anime_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=main_app.models.get_genre_default, size=None),
        ),
    ]
