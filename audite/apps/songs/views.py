from django.shortcuts import render

from audite.apps.songs.models import Artist, Album, Song
from audite.apps.songs.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import viewsets

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albumes to be viewed or edited.
    """
    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('calification')
    serializer_class = SongSerializer