from django.shortcuts import render

# Create your views here.
from .models import Musician,Album
from .serializers import MusicianSerializer,AlbumSerializer
from rest_framework import generics
class MusiciansList(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
class AlbumsList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
class MusiciansListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
class AlbumsListById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer