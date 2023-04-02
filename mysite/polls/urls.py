from django.urls import path

from . import views

#admin path
urlpatterns = [
    path('', views.index, name='index'),
]