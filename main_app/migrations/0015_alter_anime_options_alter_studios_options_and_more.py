# Generated by Django 4.0.2 on 2022-02-28 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_anime_voice_actors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={},
        ),
        migrations.AlterModelOptions(
            name='studios',
            options={'ordering': ['pk']},
        ),
        migrations.RemoveField(
            model_name='anime',
            name='voice_actors',
        ),
    ]
