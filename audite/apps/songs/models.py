from django.db import models

# Create your models here.

from . import managers

def upload_image(instance, filename):
    return 'artits/%s/%s' % (instance.username, filename)


class Artist(models.Model):
    '''
    Model for song's artist
    '''

    # Relations
    # Attributes - Mandatory
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=50, blank=True, null=True)
    # Attributes - Optional
    picture = models.ImageField(upload_to=upload_image, height_field=400, width_field=400, blank=True, null=True)
    # Object Manager
    objects = managers.ProfileManager()
    # Custom Properties

    # Methods
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
    objects = managers.ProfileManager()
    # Custom Properties
    # Methods
    # Meta and String
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("name",)
 
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
    objects = managers.ProfileManager()
    # Custom Properties

    # Methods

    # Meta and String
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ("title",)
 
    def __str__(self):
        return self.title