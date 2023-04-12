from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from .func import *
from .models import *

# Create your views here.

def admin_home(request):
    """Class view for admin home screen"""
    username = 'TEST'
    template_name = 'admin_home.html'
    return render(request, template_name, {'username': username})

class roster_prof(generic.ListView):
    """View for viewing list of professors"""
    context_object_name = 'prof_list'
    template_name = 'roster_prof.html'

    def get_queryset(self):
        return roster_prof_name()
    
def dept_index(request):
    """index for viewing departmental salaries. Can lead to a page to list of departmental professors"""
    template_name = 'dept_index.html'
    username = 'TEST'
    departments = roster_department()

    return render(request, template_name, {'departments':departments,"username":username})#'dept_max':dept_max,'dept_min':dept_min,'dept_avg':dept_avg})

def dept_overview(request,dept:str):
    """Gives view on department salary statistics and Instructors under department"""
    template_name ='dept_view.html'
    username = 'TEST'
    instructors = dept_Instructors(dept)
    max_sal = instructors.aggregate(Max('salary'))
    min_sal = instructors.aggregate(Min('salary'))
    avg_sal = instructors.aggregate(Avg('salary'))

    dictonary = {'username':username,'department':dept,'instructors':instructors}
    dictonary.update(max_sal)
    dictonary.update(min_sal)
    dictonary.update(avg_sal)
    
    return render(request, template_name, dictonary)

def course_index(request):
    template_name="course_index.html"
    username='Test'
    courses = roster_courses()
    print(courses)
    dictonary = {'username':username,'courses':courses}

    return render(request, template_name, dictonary)
