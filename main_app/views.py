from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Anime, VoiceActor, Studios, Photo
from .forms import EpisodeForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'my-cat-collector-bucket'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', { 'animes': animes })

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    studios = Studios.objects.all()
    voice_actors = VoiceActor.objects.all()
    episode_form = EpisodeForm()
    return render(request, 'animes/detail.html', { 
        'anime': anime,
        'episode_form' : episode_form,
        'studios': studios,
        'voice_actors': voice_actors
    })

def add_episode(request, anime_id):
    form = EpisodeForm(request.POST)
    if form.is_valid():
        new_episode = form.save(commit=False)
        new_episode.anime_id = anime_id
        new_episode.save()
    return redirect('detail', anime_id = anime_id)

def add_studio(request, anime_id, studio_id):
    Anime.objects.get(id=anime_id).studio.add(studio_id)
    return redirect('detail', anime_id=anime_id,)

def add_photo(request, anime_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, anime_id=anime_id)
            photo.save()
        except: 
            print('An error occurred uploading file')
    return redirect('detail', anime_id=anime_id)



def add_voice_actor(request, anime_id, voice_actor_id):
    Anime.objects.get(id=anime_id).voice_actor.add(voice_actor_id)
    return redirect('detail', anime_id=anime_id,)

def voice_actor_index(request):
    voice_actors = VoiceActor.objects.all()
    return render(request, 'voice_actors/index.html', {'voice_actors': voice_actors})

def studio_index(request):
    studios = Studios.objects.all()
    return render(request, 'studios/index.html',
    {'studios': studios})



class AnimeCreate(CreateView):
    model = Anime
    fields = ['title', 'release', 'seasons', 'episodes', 'description', 'genre', 'director']

class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['seasons', 'episodes', 'genre', 'description',]

class AnimeDelete(DeleteView):
    model = Anime
    success_url = '/anime/'

class VoiceActorCreate(CreateView):
    model = VoiceActor
    fields = ['name']
    success_url = '/voice-actors/'

class VoiceActorDelete(DeleteView):
    model= VoiceActor
    success_url = '/voice-actors/'

class StudioCreate(CreateView):
    model = Studios
    fields = ['name', 'img']
    success_url = '/studios/'

# self.title = title
#         self.description = description
#         self.release = release
#         self.seasons = seasons
#         self.episodes = episodes
#         self.studio = studio
#         self.genre = genre
#         self.director = director
#         self.img = img