from urllib.request import Request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, JsonResponse

from musicapp.models import Artiste, Song, Lyric


# Create your views here.


def artiste_list(request):
    artistes = Artiste.objects.all()
    data = {"Playlist": list(artistes.values(
        "stage_name", "first_name", "last_name", "age"))}
    return JsonResponse(data)


def artiste_details(request, pk):
    artiste_detail = get_object_or_404(Artiste, pk=pk)
    data = {"Playlist": {
        # "id": artiste_detail.id,
        "stage_name": artiste_detail.stage_name,
        "first_name": artiste_detail.first_name,
        "last_name": artiste_detail.last_name,
        "age": artiste_detail.age,
    }}
    return JsonResponse(data)


def index(request):
    my_dict = {
        'insert_content': "HELLO I'M FROM MUSICAPP!"
    }
    return render(request, 'musicapp/index.html', context=my_dict)
