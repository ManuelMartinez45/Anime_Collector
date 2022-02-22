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
    title = models.CharField(max_length=250)
    release = models.CharField(max_length=250)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    description = models.TextField(default='')
    studio = models.CharField(max_length=250)
    img = models.CharField(max_length=350)
    genre = ArrayField(models.CharField(max_length=250), default=get_genre_default)
    director = ArrayField(models.CharField(max_length=250), default=get_director_default)
    
    # description = models.TextField()

    def __str__(self):
        return self.title
# anime =[ 
#     Anime(title="Demon Slayer: Kimetsu No Yaiba", studio="Ufotable", release="2019 - Present", genre=['Dark Fantasy', 'Adventure', 'Martial Arts'], director=['Koyaharu Gotouge'], img='https://www.whats-on-netflix.com/wp-content/uploads/2021/01/demon-slayer-kimetsu-no-yaiba-season-1-coming-to-netflix.jpg', description='a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows teenage Tanjiro Kamado, who strives to become a demon slayer after his family was slaughtered and his younger sister Nezuko turned into a demon.', episodes=26, seasons=2),
#     Anime(title='Cowboy Bebop', description="Set in 2071, in a post-apocalyptic world where Earth has become largely uninhabitable, the story follows a ragtag group of bounty hunters, known as cowboys, aboard the spaceship 'Bebop'. As they traverse planets and moons in search of wanted fugitives, each cowboy contends with shadows from the past they can't outrun.",release='October 24, 1998 - April 24, 1999', seasons='1', episodes='26', studio='Sunrise', genre=['Neo-Noir', 'Space Western'], director=['Shinchiro Watanabe'], img='https://img1.hulu.com/user/v3/artwork/af54be93-ee11-475c-b786-3543a9a7d4ba?base_image_bucket_name=image_manager&base_image=9c7dd5d7-6578-41d9-abd4-57d410e62ea1&size=1200x630&format=jpeg'),
#     Anime(title='Attack On Titan', description='Set in a fantasy world, mankind is driven to the brink of extinction by mindless, man-eating giants known as Titans. In defense, all of humanity retreated to a civilisation contained within three concentric 50-meter Walls: Maria, Rose, and Sina. In the year 845, after nearly a century of relative peace within the walls, a 60-meter "Colossal" Titan materialised at and destroyed the outermost gate, ushering in hoards of smaller Titans. Witnessing the fullness of the Titan horror first-hand, a young and tenacious Eren Jaeger vows to rid the world of all Titans and win back freedom for mankind. He is joined by his adoptive sister, Mikasa Ackerman and their friend, Armin Arlert as they set out to fulfill this shared dream.', release='April 7, 2013 - Present', seasons='4', episodes='81', studio='Wit Studio, MAPPA', genre=['Action, Dark Fantasy, Post-Apocalyptic'], director=['Tetsuro Araki (1-59)', 'Masashi Koizuka (26-59)', 'Yuichiro Hayashi (60 - )', 'Jun Shishido (60 - )'], img='https://flxt.tmsimg.com/assets/p10701949_b_v8_ah.jpg'),
#     Anime(title='Durarara!!', description="Tired of his mundane life, Mikado Ryugamine decides to move to Ikebukuro, a district in Tokyo, when a friend invites him. With everything from invisible gangs to rumored beings, Ikebukuro is full of connected mysteries where people's pasts intertwine with the present", release='January 8, 2010', seasons='2', episodes='62', studio='Shuka', genre=['Action', 'Suspense', 'Urban Fantasy'], director=['Takahiro Omori'], img='https://upload.wikimedia.org/wikipedia/en/5/50/Durarara%21%21_vol01_Cover.jpg'),
#     Anime(title='Afro Samurai', description="On the dark path of swordsmanship in a 'futuristic' yet feudal Japan, it is said that the one who becomes the No. 1 warrior will rule the world with powers akin to a god. Only the No. 2 warrior is allowed to challenge the No. 1, but anyone can challenge the No. 2. The current No. 2, the Afro Samurai, travels the road looking for revenge on Justice, the man who murdered his father (who was then the No. 1) in front of him when he was just a boy, a skilled gunman who became the current No. 1 after defeating Afro's father.", release='January 4, 2007', seasons=1, episodes=5, studio='Gonzo', genre=['Action', 'Period Piece'], img='https://m.media-amazon.com/images/M/MV5BY2I2MzU0ZmUtNWE5Mi00OWM3LWIyZDEtZTg0Y2U2N2FlZDUyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
#     ]

