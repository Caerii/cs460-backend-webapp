from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .func import *
from .models import *

# Create your views here.

def student_home(request):

    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Administration').exists()):
        return redirect('/univ/')
    if(user.groups.filter(name='Instructor').exists()):
        return redirect('/instr/')

    if request.method == "POST":
        dept = (str)(request.POST.get('department'))
        sem = (int)(request.POST.get('semester'))
        yr = (int)(request.POST.get('year'))
        return redirect(reverse('stud:course_view', kwargs={'dept' : dept, 'sem' : sem, 'yr' : yr}))

    username = request.user.username
    usertype = 'student'
    template_name = 'student_home.html'
    return render(request, template_name, {'username': username, 'usertype': usertype})

def course_view(request, dept, sem, yr):

    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Administration').exists()):
        return redirect('/univ/')
    if(user.groups.filter(name='Instructor').exists()):
        return redirect('/instr/')

    template_name = 'course_view.html'
    usertype = 'student'
    course_list = section_by_year(dept, sem, yr)
    return render(request, template_name, {'course_list': course_list, 'usertype' : usertype})