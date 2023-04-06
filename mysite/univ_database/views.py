from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .func import *

# Create your views here.

class univ_index(generic.ListView):
    context_object = 'prof_list'
    template_name = 'univ_index.html'

    def get_queryset(self):
        return roster_prof_name()

        