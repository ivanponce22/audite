from django.db import models
from django.contrib.auth.models import User
from audite.apps.songs.models import Artist, Song, Album

from . import managers

# Create your models here.

def upload_image(instance, filename):
    return 'profiles/%s/%s' % (instance.username, filename)

class Profile(models.Model):
    '''Model for user profile'''

    # Relations
    user = models.OneToOneField(User)
    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    # Attributes - Optional
    favourite_artists = models.ManyToManyField(Artist, related_name='favourite_artists', blank=True)
    picture = models.ImageField(upload_to=upload_image, height_field=400, width_field=400, blank=True, null=True)
    # Object Manager
    objects = managers.ProfileManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("name",)
 
    def __str__(self):
        return self.name

class Playlist(models.Model):
    '''Model for user's playlists'''

    # Relations
    user = models.OneToOneField(Profile)
    songs = models.ManyToManyField(Song, related_name='playlist_songs', blank=True)
    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    # Attributes - Optional
    # Object Manager
    objects = managers.PlaylistManager()
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ("name",)
 
    def __str__(self):
        return self.name



