from django.contrib import admin

from.models import Anime, Studios, Episode, VoiceActor
# Register your models here.

admin.site.register(Anime)
admin.site.register(Studios)
admin.site.register(Episode)
admin.site.register(VoiceActor)
