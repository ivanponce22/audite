from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

from audite.apps.songs.views import ArtistViewSet, AlbumViewSet, SongViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albumes', AlbumViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(router.urls)),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    #apps
    url(r'^', include('audite.apps.index.urls')),
    url(r'^', include('audite.apps.songs.urls')),
    url(r'^', include('audite.apps.users_profile.urls')),
    
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
