# encoding:utf-8

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from audite.apps.users_profile.models import Playlist

class PlaylistForm(ModelForm):

    def fill_data(self, user):
        self.fields['user'] = forms.ModelChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'datos_usuario form-control'
                }
            ),
            queryset=User.objects.filter(id=user.id),
            initial=User.objects.filter(id=user.id)[0]
        )

    def clean(self):
        cleaned_data = super(PlaylistForm, self).clean()
        name = cleaned_data.get("name")
        user = cleaned_data.get("user")

        if Playlist.objects.filter(user__id=user.id, name=name).first() is not None:
            raise forms.ValidationError("The playlist exists actually")

    class Meta:
        model = Playlist
        fields = ('name', 'user',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name playlist'}),
        }