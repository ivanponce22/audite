from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'albumes', views.AlbumViewSet)
router.register(r'songs', views.SongViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]