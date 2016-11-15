# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 03:46
from __future__ import unicode_literals

import audite.apps.users_profile.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.SlugField(blank=True, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('songs', models.ManyToManyField(blank=True, related_name='playlist_songs', to='songs.Song')),
            ],
            options={
                'verbose_name_plural': 'Playlists',
                'verbose_name': 'Playlist',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('picture', models.ImageField(blank=True, height_field=400, null=True, upload_to=audite.apps.users_profile.models.upload_image, width_field=400)),
                ('favourite_artists', models.ManyToManyField(blank=True, related_name='favourite_artists', to='songs.Artist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'verbose_name': 'Profile',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users_profile.Profile'),
        ),
    ]
