from django.conf.urls import url, include

from .views import SongsListView, ArtistListView, ArtistDetailView



urlpatterns = [
    url(r'^songs/$', SongsListView.as_view(), name='songs'),
    url(r'^artists/$', ArtistListView.as_view(), name='artists'),
    url(r'^artist/(?P<artist_name_slug>[\w-]+)/$', ArtistDetailView.as_view(), name='artist_detail'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]