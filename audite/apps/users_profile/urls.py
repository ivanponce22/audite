from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from audite.apps.users_profile.views import PlaylistCreateView, PlayListAllView, PlaylistDetailView, AddSongToPlaylist, AddFavouriteArtist

urlpatterns = [
    url(r'^new_playlist/$', login_required(PlaylistCreateView.as_view()), name='new_playlist'),
    url(r'^playlist/(?P<playlist_slug>[\w-]+)/$', login_required(PlaylistDetailView.as_view()), name='playlist'),
    url(r'^add_song/(?P<playlist_id>[\w-]+)/(?P<song_id>[\w-]+)/$', login_required(AddSongToPlaylist.as_view()), name='add_song'),
    url(r'^playlists_all/$', login_required(PlayListAllView.as_view()), name='playlists_all'),
    url(r'^add_favourite_artist/(?P<artist_id>[0-9]+)/$', login_required(AddFavouriteArtist.as_view()), name='add_favourite_artist'),
]
