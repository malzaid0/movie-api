from django.shortcuts import render
import requests


# Create your views here.
def list(request):
    query = request.GET.get('search_term')
    response = requests.get(f"http://www.omdbapi.com/?apikey=a7558e05&s=avengers").json()
    context = {
        "movies": response,
    }
    return render(request, 'search.html', context)


def detail(request, movie_id):
    movie = requests.get(f"http://www.omdbapi.com/?apikey=a7558e05&i={movie_id}").json()
    context = {
        "movie": movie,
    }
    return render(request, 'detail.html', context)
