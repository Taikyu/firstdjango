
from django.contrib import admin
from django.urls import path

from musicapp import views

from .views import artiste_list, artiste_details
from .apiviews import ArtisteList, ArtisteDetail, ArtisteCreateView, ArtisteUpdateView, ArtisteDeleteView, SongList, SongDetail


urlpatterns = [
    path('', views.index, name='index'),
    # path('artistes/', views.artiste_list, name='artiste_list'),
    # path('artistes/<int:pk>', views.artiste_details, name='artiste_details'),
    path('artiste/', ArtisteList.as_view(), name='artiste_list'),
    path('artiste/create/', ArtisteCreateView.as_view(), name='artiste_create'),
    path('artiste/<str:pk>/', ArtisteDetail.as_view(), name='artiste_details'),
    path('artiste/song', SongList.as_view(), name='song_list'),
    path('artiste/song/<str:pk>/', SongDetail.as_view(), name='song_details'),
    # path('artiste/create/', ArtisteCreateView.as_view(), name='artiste_new'),
    path('artiste/<str:pk>/edit/', ArtisteUpdateView.as_view(), name='artiste_edit'),
    path('artiste/<str:pk>/delete',
         ArtisteDeleteView.as_view(), name='artiste_delete')
]
