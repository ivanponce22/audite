from django.db import models
import time
# Create your models here.

from . import managers

def upload_image(instance, filename):
    return 'artits/%s/%s' % (filename)


class Artist(models.Model):
    '''
    Model for song's artist
    '''

    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    # Attributes - Optional
    picture = models.ImageField(upload_to=upload_image, height_field=400, width_field=400, blank=True, null=True)
    # Object Manager
    objects = managers.ArtistManager()

    # Methods

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(self.__class__, self).save(*args, **kwargs)

    def get_songs(self):
        return Song.objects.filter(album__artist=self)

    def get_albums(self):
        return Album.objects.filter(artist=self)


    # Meta and String
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ("name",)
 
    def __str__(self):
        return self.name

class Album(models.Model):
    '''
    Model for song's Album
    '''

    # Relations
    artist = models.ForeignKey(Artist)
    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    # Attributes - Optional
    genre = models.CharField(max_length=60, blank=True, null=True)
    # Object Manager
    objects = managers.AlbumManager()

    # Methods
    def get_songs(self):
        return Song.objects.filter(album=self)

    # Meta and String
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("-year", "name")
 
    def __str__(self):
        return self.name

class Song (models.Model):
    '''
    Model for song
    '''

    # Relations
    album = models.ForeignKey(Album)
    # Attributes - Mandatory
    title = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    # Attributes - Optional
    duration = models.IntegerField(default=0)
    calification = models.IntegerField(default=0)
    # Object Manager
    objects = managers.SongManager()
    # Custom Properties

    # Methods
    def get_duration(self):
        return time.strftime("%M:%S", time.gmtime(self.duration))

    # Meta and String
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ("title",)
 
    def __str__(self):
        return self.title