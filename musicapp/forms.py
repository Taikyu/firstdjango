from django import forms
from .models import Artiste, Song, Lyric


class ArtisteForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = '__all__'
