from audite.apps.songs.models import Artist, Album, Song
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'name_slug', 'picture')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'name', 'year', 'name_slug', 'genre')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('album', 'title', 'name_slug', 'duration', 'calification')
