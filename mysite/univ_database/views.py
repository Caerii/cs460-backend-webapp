from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def univ_index(request):
    return HttpResponse('university_database_index')