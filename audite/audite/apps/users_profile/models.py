from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from audite.apps.songs.models import Artist, Song, Album
from django.db.models.signals import post_save
import time

from . import managers

from audite.apps.users_profile.tasks import send_email

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
    def get_favourite_artists (self):
        return self.favourite_artists.all()

    def get_playlists(self):
        return Playlist.objects.filter(user=self)


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
    user = models.ForeignKey(User)
    songs = models.ManyToManyField(Song, related_name='playlist_songs', blank=True)
    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    # Object Manager
    objects = managers.PlaylistManager()
    
    # Methods
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(self.__class__, self).save(*args, **kwargs)

    def get_duration(self):
        time_duration = 0
        for song in self.songs.all():
            time_duration = time_duration + song.duration
        return time.strftime("%H:%M:%S", time.gmtime(time_duration))

    def get_calification(self):
        total_calification = 0
        for song in self.songs.all():
            total_calification = total_calification + song.calification
        return int(total_calification/len(self.songs.all()))

    # Meta and String
    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ("name",)
 
    def __str__(self):
        return self.name

def send_email_notification(sender, **kwargs):
    playlist = kwargs["instance"]
    send_email.delay(playlist.user.username, playlist.name, playlist.user.email)

post_save.connect(send_email_notification, sender=Playlist)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile()
        profile.user = user
        profile.name = user.username
        profile.save()

post_save.connect(create_profile, sender=User)



