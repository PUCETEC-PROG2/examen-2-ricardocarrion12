from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.order_by('genre')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))


def movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))