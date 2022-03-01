from django.forms import ModelForm
from .models import Episode

class EpisodeForm(ModelForm):
    class Meta: 
        model = Episode
        fields = ['title', 'director', 'air_date', 'eng_air_date']