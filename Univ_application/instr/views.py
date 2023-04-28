from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .func import *
from .models import *

# Create your views here.

def instructor_home(request):

    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Administration').exists()):
        return redirect('/univ/')
    if(user.groups.filter(name='Student').exists()):
        return redirect('/stud/')

    if request.method == "POST":

        if 'sec_query' in request.POST:
            sem = (int)(request.POST.get('semester'))
            name = (str)(request.POST.get('name'))
            return redirect(reverse('instr:sections_view', kwargs={'sem' : sem, 'name' : name}))
        elif 'stud_query' in request.POST:
            cour = (str)(request.POST.get('course'))
            sec = (str)(request.POST.get('section'))
            sem = (int)(request.POST.get('semester2'))
            yr = (int)(request.POST.get('year'))
            return redirect(reverse('instr:student_view', kwargs={'cour' : cour, 'sec' : sec, 'sem' : sem, 'yr' : yr}))

    username = request.user.username
    usertype = 'instructor'
    template_name = 'instructor_home.html'
    return render(request, template_name, {'username': username, 'usertype': usertype})

def sections_view(request, sem, name):

    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Administration').exists()):
        return redirect('/univ/')
    if(user.groups.filter(name='Student').exists()):
        return redirect('/stud/')

    template_name = 'sections_view.html'
    section_list = sections_by_prof(sem, name)
    return render(request, template_name, {'section_list' : section_list})

def student_view(request, cour, sec, sem, yr):

    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Administration').exists()):
        return redirect('/univ/')
    if(user.groups.filter(name='Student').exists()):
        return redirect('/stud/')

    template_name = 'student_view.html'
    student_list = students_by_section(cour, sec, sem, yr)
    return render(request, template_name, {'student_list' : student_list})