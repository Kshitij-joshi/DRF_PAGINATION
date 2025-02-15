from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework import viewsets
from .models import Moviedata , Movies

from django.core.paginator import Paginator



# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class FamilyViewSet(viewsets.ModelViewSet):
     queryset = Moviedata.objects.filter(category="family")
     serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(category="comedy")
    serializer_class = MovieSerializer


def movie_list(request):
    movies_object = Movies.objects.all()
    paginator = Paginator(movies_object,2)
    page = request.GET.get('page')
    movies_object = paginator.get_page(page)
    return render(request,'movies/allmovies.html',{"movies_object":movies_object})

