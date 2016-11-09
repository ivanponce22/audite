from django.views.generic import DetailView, UpdateView, View, CreateView, ListView
from django.shortcuts import render

from audite.apps.users_profile.models import Playlist
from audite.apps.users_profile.forms import PlaylistForm
from audite.apps.songs.models import Song, Artist

# Create your views here.

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'user/create_playlist.html'

    def get(self):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.fill_data(request.user)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return '/playlists_all/'


class PlayListAllView(ListView):

    model = Playlist
    template_name = 'user/playlists_all.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['object_list'] = self.request.user.profile.get_playlists()
        context['favourite_artists'] = self.request.user.userprofile.get_favourite_artists()
        return context

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'user/playlist.html'
    slug_url_kwarg = 'playlist_slug'
    slug_field = 'name_slug'

#agregar a la lista
class AddSongToPlaylist(View):

    def get(self, request, *args, **kwargs):
        song = Song.objects.get(id=self.kwargs['song_id'])
        playlist = Playlist.objects.get(id=self.kwargs['playlist_id'])
        playlist.songs.add(song)
        playlist.save()
        return HttpResponse("Added!")


#agregar artista favorito
class AddFavouriteArtist(View):

    def get(self, request, *args, **kwargs):
        artist = Artist.objects.get(id=self.kwargs['artist_id'])
        request.user.following.add(user_to_folow)
        return HttpResponse("Added!")
