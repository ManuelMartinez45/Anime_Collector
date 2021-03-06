# Generated by Django 4.0.2 on 2022-02-17 03:30

import django.contrib.postgres.fields
from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_anime_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='director',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=main_app.models.get_director_default, size=None),
        ),
    ]
