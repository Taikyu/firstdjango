from rest_framework import serializers
from .models import Artiste, Song, Lyric


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    lyric = LyricSerializer(many=True, required=False)

    class Meta:
        model = Song
        fields = '__all__'


class ArtisteSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Artiste
        fields = '__all__'
