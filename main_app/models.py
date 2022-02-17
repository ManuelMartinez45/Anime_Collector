from django.db import models
from django.contrib.postgres.fields import ArrayField

# self.title = title
#         self.description = description
#         self.release = release
#         self.seasons = seasons
#         self.episodes = episodes
#         self.studio = studio
#         self.genre = genre
#         self.director = director
#         self.img = img
# Create your models here.
def get_genre_default():
    return list('')

def get_director_default():
    return list('')


class Anime(models.Model):
    title = models.CharField(max_length=150)
    release = models.CharField(max_length=150)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    description = models.TextField(default='')
    studio = models.CharField(max_length=150)
    img = models.CharField(max_length=150)
    genre = ArrayField(models.CharField(max_length=150), default=get_genre_default)
    director = ArrayField(models.CharField(max_length=150), default=get_director_default)
    
    # description = models.TextField()

    def __str__(self):
        return self.title


# anime = Anime(title="Demon Slayer: Kimetsu No Yaiba", studio="Ufotable", release="2019 - Present", genre=['Dark Fantasy', 'Adventure', 'Martial Arts'], director=['Koyaharu Gotouge'], img='https://www.whats-on-netflix.com/wp-content/uploads/2021/01/demon-slayer-kimetsu-no-yaiba-season-1-coming-to-netflix.jpg', description='a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows teenage Tanjiro Kamado, who strives to become a demon slayer after his family was slaughtered and his younger sister Nezuko turned into a demon.', episodes=26, seasons=2)