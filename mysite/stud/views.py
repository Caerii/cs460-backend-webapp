from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .func import *
from .models import *

# Create your views here.

def student_home(request):
    if request.method == "POST":
        sem = (int)(request.POST.get('semester'))
        yr = (int)(request.POST.get('year'))
        return redirect(reverse('stud:course_view', kwargs={'sem' : sem, 'yr' : yr}))

    username = 'TEST'
    usertype = 'student'
    template_name = 'student_home.html'
    return render(request, template_name, {'username': username, 'usertype': usertype})

def course_view(request, sem, yr):

    template_name = 'course_view.html'
    course_list = section_by_year(sem, yr)
    return render(request, template_name, {'course_list': course_list})