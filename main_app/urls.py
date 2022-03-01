from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('anime/', views.anime_index, name='index'),
    path('anime/<int:anime_id>/', views.anime_detail, name='detail'),
    path('anime/create/', views.AnimeCreate.as_view(), name='anime_create'),
    path('anime/<int:pk>/update/', views.AnimeUpdate.as_view(), name='anime_update'),
    path('anime/<int:pk>/delete/', views.AnimeDelete.as_view(), name='anime_delete'),
    path('anime/<int:anime_id>/add_episode', views.add_episode, name='add_episode'),
    path('anime/<int:anime_id>/add_studio/<int:studio_id>/', views.add_studio, name='add_studio'),
    path('anime/<int:anime_id>/add_voice_actor/<int:voice_actor_id>/', views.add_voice_actor, name='add_voice_actor'),
    path('anime/<int:anime_id>/add_photo', views.add_photo, name='add_photo'),
    path('voice-actors/', views.voice_actor_index, name='voice_actor_index'),
    path('voice-actor-create/', views.VoiceActorCreate.as_view(), name='voice_actor_create'),
    path('voice-actor/<int:pk>/delete/', views.VoiceActorDelete.as_view(), name='voice_actor_delete'),
    path('studios/', views.studio_index, name='studio_index'),
    path('studios-create/', views.StudioCreate.as_view(), name='studio_create')
]