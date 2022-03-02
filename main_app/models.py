from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

def get_genre_default():
    return list('')

def get_director_default():
    return list('')


class VoiceActor(models.Model):
    name = models.CharField(max_length=250)
    img= models.CharField(max_length=200, default='')
    # animes =  models.ManyToManyField(Anime, default='0') 


class Studios(models.Model):
    name=models.CharField(max_length=200)
    img= models.CharField(max_length=350, default='')
    # anime = models.ManyToManyField(Anime, default=0)
    
    def __str__(self):
        return f"Studios(name='{self.name}', img='{self.img}'"

    class Meta:
        ordering=['pk']

class Anime(models.Model):
    title = models.CharField(max_length=250)
    release = models.CharField(max_length=250)
    seasons = models.IntegerField()
    episodes = models.IntegerField(default='0')
    description = models.TextField(default='')
    genre = ArrayField(models.CharField(max_length=250), default=get_genre_default)
    director = ArrayField(models.CharField(max_length=250), default=get_director_default)
    studio = models.ManyToManyField(Studios)
    voice_actor = models.ManyToManyField(VoiceActor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id': self.id})


class Episode(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=250)
    air_date = models.DateField('Original Air Date')
    eng_air_date = models.DateField('English Air Date')

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.anime}/ episode title: {self.title}'

class Photo(models.Model):
    url = models.CharField(max_length=350)
    anime = models.ForeignKey(Anime, on_delete = models.CASCADE)



# anime =[ 
#     Anime(title="Demon Slayer: Kimetsu No Yaiba", release="2019 - Present", genre=['Dark Fantasy', 'Adventure', 'Martial Arts'], director=['Koyaharu Gotouge'], description='a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows teenage Tanjiro Kamado, who strives to become a demon slayer after his family was slaughtered and his younger sister Nezuko turned into a demon.', episodes=26, seasons=2),
#     Anime(title='Cowboy Bebop', description="Set in 2071, in a post-apocalyptic world where Earth has become largely uninhabitable, the story follows a ragtag group of bounty hunters, known as cowboys, aboard the spaceship 'Bebop'. As they traverse planets and moons in search of wanted fugitives, each cowboy contends with shadows from the past they can't outrun.",release='October 24, 1998 - April 24, 1999', seasons='1', episodes='26', genre=['Neo-Noir', 'Space Western'], director=['Shinchiro Watanabe']),
#     
# Anime(title='Attack On Titan', description='Set in a fantasy world, mankind is driven to the brink of extinction by mindless, man-eating giants known as Titans. In defense, all of humanity retreated to a civilisation contained within three concentric 50-meter Walls: Maria, Rose, and Sina. In the year 845, after nearly a century of relative peace within the walls, a 60-meter "Colossal" Titan materialised at and destroyed the outermost gate, ushering in hoards of smaller Titans. Witnessing the fullness of the Titan horror first-hand, a young and tenacious Eren Jaeger vows to rid the world of all Titans and win back freedom for mankind. He is joined by his adoptive sister, Mikasa Ackerman and their friend, Armin Arlert as they set out to fulfill this shared dream.', release='April 7, 2013 - Present', seasons='4', episodes='81', genre=['Action, Dark Fantasy, Post-Apocalyptic'], director=['Tetsuro Araki (1-59)', 'Masashi Koizuka (26-59)', 'Yuichiro Hayashi (60 - )', 'Jun Shishido (60 - )']),
#     Anime(title='Durarara!!', description="Tired of his mundane life, Mikado Ryugamine decides to move to Ikebukuro, a district in Tokyo, when a friend invites him. With everything from invisible gangs to rumored beings, Ikebukuro is full of connected mysteries where people's pasts intertwine with the present", release='January 8, 2010', seasons='2', episodes='62', genre=['Action', 'Suspense', 'Urban Fantasy'], director=['Takahiro Omori'],

#     Anime(title='Afro Samurai', description="On the dark path of swordsmanship in a 'futuristic' yet feudal Japan, it is said that the one who becomes the No. 1 warrior will rule the world with powers akin to a god. Only the No. 2 warrior is allowed to challenge the No. 1, but anyone can challenge the No. 2. The current No. 2, the Afro Samurai, travels the road looking for revenge on Justice, the man who murdered his father (who was then the No. 1) in front of him when he was just a boy, a skilled gunman who became the current No. 1 after defeating Afro's father.", release='January 4, 2007', seasons=1, episodes=5, genre=['Action', 'Period Piece'])
#     ]

