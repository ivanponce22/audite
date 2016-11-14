from django.views.generic import DetailView, UpdateView, View, CreateView, ListView
from django.shortcuts import render

from audite.apps.users_profile.models import Playlist, Profile
from audite.apps.users_profile.forms import PlaylistForm
from audite.apps.songs.models import Song, Artist

from django.http import HttpResponse
from django.conf import settings
import pusher

# Create your views here.


pusher_client = pusher.Pusher(app_id=str(settings.PUSHER_APP_ID),key=str(settings.PUSHER_KEY_ID) ,secret=str(settings.PUSHER_SECRET) ,ssl=True)

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
        profile_user = list(Profile.objects.filter(user = self.request.user))
        context['object_list'] = Playlist.objects.filter(user = self.request.user)
        if(len(profile_user)>0):
            context['favourite_artists'] = profile_user[0].get_favourite_artists()
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
        pusher_client.trigger('channel_'+str(self.request.user.id), 'add_song', {'message': 'song '+song.title+' added to playlist '+playlist.name})
        return HttpResponse("Added!")


#agregar artista favorito
class AddFavouriteArtist(View):

    def get(self, request, *args, **kwargs):
        artist = Artist.objects.get(id=self.kwargs['artist_id'])
        request.user.following.add(user_to_folow)
        return HttpResponse("Added!")
