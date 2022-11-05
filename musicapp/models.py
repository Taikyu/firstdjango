from django.db import models
from datetime import datetime
from unittest.util import _MAX_LENGTH


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=4000)

    def __str__(self):
        return self.Song
