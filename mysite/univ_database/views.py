from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .func import *
from .models import *

# Create your views here.

class univ_index(generic.ListView):
    """Currently a test for displaying tables right now, later can be changed to redirect to the correct home"""
    context_object_name = 'prof_list'
    template_name = 'univ_index.html'
    def get_queryset(self):
        return roster_prof_name()
    
def admin_home(request):
    """Class view for admin home screen"""
    username = 'TEST'
    template_name = 'admin_home.html'
    return render(request, template_name, {'username': username})



        