from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
import time
# Create your models here.

from . import managers

def upload_image(filename):
    return 'audite/media/artits/%s' % (filename)


class Artist(models.Model):
    '''
    Model for song's artist
    '''

    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    # Attributes - Optional
    picture = models.ImageField(
        upload_to="artists", 
        blank=True, 
        null=True, 
        editable=True,)
    # Object Manager
    objects = managers.ArtistManager()

    # Methods
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)

        super(self.__class__, self).save(*args, **kwargs)

        if self.picture:
            image = Image.open(self.picture)
            (width, height) = image.size     
            size = (200, 200)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(self.picture.path)

        

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
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(self.__class__, self).save(*args, **kwargs)

    def get_songs(self):
        return Song.objects.filter(album=self)

    def get_duration(self):
        total_time = 0
        for song in self.get_songs():
            total_time = total_time + song.duration
        return time.strftime("%H:%M:%S", time.gmtime(total_time))

    def get_calification(self):
        total_calification = 0
        for song in self.get_songs():
            total_calification = total_calification + song.calification
        return int(total_calification/len(self.get_songs()))

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
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.title)
        super(self.__class__, self).save(*args, **kwargs)

    def get_duration(self):
        return time.strftime("%M:%S", time.gmtime(self.duration))

    # Meta and String
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ("title",)
 
    def __str__(self):
        return self.title