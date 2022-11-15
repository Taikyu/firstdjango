from urllib import response
from urllib.request import Request

from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        "List": "/artiste_list/",
        "Detail": "/artiste_detail/<str:pk>/",
        "Create": "/artiste_create/",
        "Update": "/artiste_update/<str:pk>/",
        "Delete": "/artiste_delete/<str:pk>/",
        "List.": "/song_list/",
        "Detail.": "/song_detail/<str:pk>/",
        "Create.": "/song_create/",
        "Update.": "/song_update/<str:pk>/",
        "Delete.": "/song_delete/<str:pk>/",

    }
    return Response(api_urls)


@api_view(['GET'])
def artisteList(request):
    artistes = Artiste.objects.all()
    serializer = ArtisteSerializer(artistes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artisteDetail(request, pk):
    artistes = Artiste.objects.get(id=pk)
    serializer = ArtisteSerializer(artistes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def artisteCreate(request):
    serializer = ArtisteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def artisteUpdate(request, pk):
    artiste = Artiste.objects.get(id=pk)
    serializer = ArtisteSerializer(instance=artiste, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def artisteDelete(request, pk):
    artiste = Artiste.objects.get(id=pk)
    artiste.delete

    return Response("Artiste has been deleted successfully!")


@api_view(['GET'])
def songList(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def songDetail(request, pk):
    songs = Song.objects.get(id=pk)
    serializer = SongSerializer(songs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def songCreate(request):
    serializer = SongSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def songUpdate(request, pk):
    song = Song.objects.get(id=pk)
    serializer = ArtisteSerializer(instance=song, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def songDelete(request, pk):
    song = Song.objects.get(id=pk)
    song.delete

    return Response("Song has been deleted successfully!")
