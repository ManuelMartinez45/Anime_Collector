from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Anime

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

class AnimeCreate(CreateView):
    model = Anime
    fields = '__all__'

class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['seasons', 'episodes', 'genre', 'description',]

class AnimeDelete(DeleteView):
    model = Anime
    success_url = '/cats/'


# self.title = title
#         self.description = description
#         self.release = release
#         self.seasons = seasons
#         self.episodes = episodes
#         self.studio = studio
#         self.genre = genre
#         self.director = director
#         self.img = img