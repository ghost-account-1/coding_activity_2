import pytz
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from app.models import Movies
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            self.object = self.get_object()
            self.object.like_movie()
            return JsonResponse({'likes':self.object.like}, status=200)
        else:
            return response

class MovieList(ListView):
    model = Movies
    paginate_by = 3

    def get_queryset(self):
        #set timezone to Asia/Manila
        timezone.activate(pytz.timezone("Asia/Manila"))
        self.request.session.setdefault('history', []).append(timezone.localtime(timezone.now()).strftime('%b %d %Y, %H:%M:%S'))
        self.request.session.modified = True
        history = self.request.session['history']
        if len(history) > 1:
            messages.add_message(self.request, messages.INFO, 'Welcome back! You’ve visited this page last '+ history[-2])
        else:
            messages.add_message(self.request, messages.INFO, 'Welcome to our site!')
        print(history)
        return self.model.objects.all().filter(is_active=True)

class MovieDetail(DetailView):
    model = Movies
    context_object_name = 'movie_details'

class MovieAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Movies
    fields = ['title']
    success_message = '%(title)s successfully created!'

class MovieEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Movies
    fields = ['title']
    template_name_suffix = '_update_form'
    success_message = '%(title)s successfully edited!'

class MovieLike(AjaxableResponseMixin, UpdateView):
    model = Movies
    fields = ['like']
    template_name_suffix = '_like_form'

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movies
    success_url = reverse_lazy('list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())
