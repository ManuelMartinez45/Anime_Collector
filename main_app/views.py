from django.shortcuts import render
from .models import Anime

# class Anime:
#     def __init__(self, title, description, release, seasons, episodes, studio, genre, director, img ):
#         self.title = title
#         self.description = description
#         self.release = release
#         self.seasons = seasons
#         self.episodes = episodes
#         self.studio = studio
#         self.genre = genre
#         self.director = director
#         self.img = img
# animes= [
#     Anime('Demon Slayer: Kimetsu no Yaiba', 'a Japanese manga series written and illustrated by Koyoharu Gotouge. It follows teenage Tanjiro Kamado, who strives to become a demon slayer after his family was slaughtered and his younger sister Nezuko turned into a demon.', '2019 - Present', '2', '26', 'Ufotable', ['Dark Fantasy', 'Adventure', 'Martial Arts'], ['Koyaharu Gotouge'],'https://www.whats-on-netflix.com/wp-content/uploads/2021/01/demon-slayer-kimetsu-no-yaiba-season-1-coming-to-netflix.jpg'
#     ),
#     Anime('Cowboy Bebop', "Set in 2071, in a post-apocalyptic world where Earth has become largely uninhabitable, the story follows a ragtag group of bounty hunters, known as cowboys, aboard the spaceship “Bebop.” As they traverse planets and moons in search of wanted fugitives, each cowboy contends with shadows from the past they can't outrun.",'October 24, 1998 - April 24, 1999', '1', '26', 'Sunrise', ['Neo-Noir', 'Space Western'], ['Shinchiro Watanabe'], 'https://img1.hulu.com/user/v3/artwork/af54be93-ee11-475c-b786-3543a9a7d4ba?base_image_bucket_name=image_manager&base_image=9c7dd5d7-6578-41d9-abd4-57d410e62ea1&size=1200x630&format=jpeg'
#     ),
#     Anime('Attack On Titan', 'Set in a fantasy world, mankind is driven to the brink of extinction by mindless, man-eating giants known as Titans. In defense, all of humanity retreated to a civilisation contained within three concentric 50-meter Walls: Maria, Rose, and Sina. In the year 845, after nearly a century of relative peace within the walls, a 60-meter "Colossal" Titan materialised at and destroyed the outermost gate, ushering in hoards of smaller Titans. Witnessing the fullness of the Titan horror first-hand, a young and tenacious Eren Jaeger vows to rid the world of all Titans and win back freedom for mankind. He is joined by his adoptive sister, Mikasa Ackerman and their friend, Armin Arlert as they set out to fulfill this shared dream.', 'April 7, 2013 - Present', '4', '81', 'Wit Studio, MAPPA', ['Action, Dark Fantasy, Post-Apocalyptic'], ['Tetsuro Araki (1-59)', 'Masashi Koizuka (26-59)', 'Yuichiro Hayashi (60 - )', 'Jun Shishido (60 - )'], 'https://flxt.tmsimg.com/assets/p10701949_b_v8_ah.jpg'
#     ),
#     Anime('Durarara!!', "Tired of his mundane life, Mikado Ryugamine decides to move to Ikebukuro, a district in Tokyo, when a friend invites him. With everything from invisible gangs to rumored beings, Ikebukuro is full of connected mysteries where people's pasts intertwine with the present", 'January 8, 2010', '2', '62', 'Shuka', ['Action', 'Suspense', 'Urban Fantasy'], ['Takahiro Omori'], 'https://upload.wikimedia.org/wikipedia/en/5/50/Durarara%21%21_vol01_Cover.jpg'   )
# ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', { 'animes': animes })

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', { 'anime': anime })