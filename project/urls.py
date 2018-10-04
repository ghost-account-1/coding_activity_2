"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import MovieList, MovieDetail, MovieAdd, MovieEdit, MovieDelete, MovieLike

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', MovieList.as_view(), name='list'),
    path('details/<int:pk>/', MovieDetail.as_view(), name='detail'),
    path('add/', MovieAdd.as_view(), name='add'),
    path('edit/<int:pk>/', MovieEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', MovieDelete.as_view(), name='delete'),
    path('like/<int:pk>/', MovieLike.as_view(), name='like'),
]
