# Generated by Django 4.0.2 on 2022-02-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_studios_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='studios',
            name='img',
            field=models.CharField(default='', max_length=350),
        ),
    ]