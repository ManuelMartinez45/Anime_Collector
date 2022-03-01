# Generated by Django 4.0.2 on 2022-02-27 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_anime_episodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='anime',
            name='img',
        ),
        migrations.AlterField(
            model_name='voiceactor',
            name='animes',
            field=models.ManyToManyField(default='0', to='main_app.Anime'),
        ),
        migrations.AlterField(
            model_name='voiceactor',
            name='img',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Studio',
        ),
        migrations.AddField(
            model_name='studios',
            name='anime',
            field=models.ManyToManyField(default=0, to='main_app.Anime'),
        ),
    ]
