from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class MovieDelete(AjaxableResponseMixin, DeleteView):
    model = Movies
    success_url = reverse_lazy('list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())
