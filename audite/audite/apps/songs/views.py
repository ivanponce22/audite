from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from audite.apps.songs.models import Artist, Album, Song
from audite.apps.users_profile.models import Playlist
from django.views.generic import DetailView, View
from django.views.generic.list import ListView
from audite.apps.songs.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import viewsets

# Views for API
class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albumes to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    permission_classes = (AllowAny,)

    queryset = Song.objects.all().order_by('calification')
    serializer_class = SongSerializer


#Views for Frontend Application
class SongsListView(ListView):
    model = Song
    template_name = 'songs/songs.html'

    def get_context_data(self, **kwargs):
        context = super(SongsListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['playlists'] = Playlist.objects.filter(user = self.request.user)
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'songs/artists.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        return context


class ArtistDetailView(DetailView):

    model = Artist
    template_name = 'songs/artist_profile.html'
    slug_url_kwarg = 'artist_name_slug'
    slug_field = 'name_slug'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(artist=self.object)
        context['songs'] = Song.objects.filter(album__artist=self.object)
        if self.request.user.is_authenticated():
            context['playlists'] = Playlist.objects.filter(user = self.request.user)
        return context
