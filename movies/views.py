from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    #It's going to have a 'queryset' and a 'serializer_class'
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(catagory = 'action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(catagory = 'comedy')
    serializer_class = MovieSerializer

