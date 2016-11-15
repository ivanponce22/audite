from django.apps import AppConfig
from django.contrib import algoliasearch

from .index import SongIndex

class SongsConfig(AppConfig):
    name = 'audite.apps.songs'

    def ready(self):
        Song = self.get_model('Song')
        algoliasearch.register(Song, SongIndex)