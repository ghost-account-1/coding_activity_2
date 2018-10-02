from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
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

class MovieAdd(SuccessMessageMixin, CreateView):
    model = Movies
    fields = ['title']
    success_message = '%(title)s successfully created!'

class MovieEdit(SuccessMessageMixin, UpdateView):
    model = Movies
    fields = ['title']
    template_name_suffix = '_update_form'
    success_message = '%(title)s successfully edited!'
