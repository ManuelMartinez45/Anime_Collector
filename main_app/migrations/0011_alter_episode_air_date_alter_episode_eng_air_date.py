# Generated by Django 4.0.2 on 2022-02-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_studios_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='episode',
            name='eng_air_date',
            field=models.DateField(),
        ),
    ]
