from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from app.models import Movies


# Create your views here.
class MovieList(ListView):
    model = Movies
    paginate_by = 3

    def get_queryset(self):
        return self.model.objects.all().filter(is_active=True)

class MovieDetail(DetailView):
    model = Movies
    context_object_name = 'movie_details'
