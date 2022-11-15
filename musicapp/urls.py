
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('artiste-list/', views.artisteList, name='artiste-list'),
    path('artiste-detail/<str:pk>/', views.artisteDetail, name='artiste-detail'),
    path('artiste-create/', views.artisteCreate, name='artiste-create'),
    path('artiste-update/<str:pk>', views.artisteUpdate, name='artiste-update'),
    path('artiste-delete/<str:pk>', views.artisteDelete, name='artiste-delete'),
    path('song-list/', views.songList, name='song-list'),
    path('song-detail/<str:pk>/', views.songDetail, name='song-detail'),
    path('song-create/', views.songCreate, name='song-create'),
    path('song-update/<str:pk>/', views.songUpdate, name='song-update'),
    path('song-delete/<str:pk>/', views.songDelete, name='song-delete'),
]
