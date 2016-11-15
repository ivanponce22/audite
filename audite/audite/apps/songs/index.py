from django.contrib.algoliasearch import AlgoliaIndex

class SongIndex(AlgoliaIndex):
    fields = ('title', 'album', 'duration', 'calification')
    settings = {'attributesToIndex': ['title']}
    index_name = 'song_index'