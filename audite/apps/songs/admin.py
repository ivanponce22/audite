from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):

    list_display = ("name", "name_slug", "picture")
    search_fields = ["name"]

@admin.register(models.Album)
class ALbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "name", "name_slug", "year", "genre")
    search_fields = ["name", "year", "genre"]

@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("album", "title", "name_slug", "duration", "calification")
    search_fields = ["album", "title", "calification"]