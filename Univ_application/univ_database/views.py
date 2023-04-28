from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.db import DatabaseError
from .form import *
from .func import *
from .models import *

# Create your views here.

def admin_home(request):
    """Class view for admin home screen"""
    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Student').exists()):
       return redirect('/stud/')
    if(user.groups.filter(name='Instructor').exists()):
       return redirect('/instr/')
    username = request.user.username
    usertype = 'administration'
    template_name = 'admin_home.html'
    return render(request, template_name, {'username': username , 'usertype':usertype})

def prof_index(request):
    """View for viewing list of professors"""
    post=request.method
    print(post)
    template_name = 'roster_prof.html'
    if request.method == "GET":
        sort=instr_sort1(request.GET)
        print('dam')
        print(sort['sort'].value())
        if 'sort' in request.GET:
            print('yea')
            prof_list=roster_prof(sort['sort'].value())
            print(sort['sort'].value())
        else:
            prof_list=roster_prof('name')
    else:
        sort=instr_sort1()
        prof_list=roster_prof('name')

    return render(request, template_name, {'prof_list':prof_list , 'sort':sort})
    
def dept_index(request):
    """index for viewing departmental salaries. Can lead to a page to list of departmental professors"""
    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Student').exists()):
        return redirect('/stud/')
    if(user.groups.filter(name='Instructor').exists()):
        return redirect('/instr/')
    template_name = 'dept_index.html'
    username = request.user.username
    departments = roster_department()

    return render(request, template_name, {'departments':departments})#'dept_max':dept_max,'dept_min':dept_min,'dept_avg':dept_avg})

def dept_overview(request,dept:str):
    """Gives view on department salary statistics and Instructors under department"""
    user = request.user
    if(not user.is_authenticated):
        return redirect('/accounts/login')
    if(user.groups.filter(name='Student').exists()):
        return redirect('/stud/')
    if(user.groups.filter(name='Instructor').exists()):
        return redirect('/instr/')
    template_name ='dept_view.html'
    username = request.user.username
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
    if(not request.user.is_authenticated):
        return redirect('/accounts/login')
    template_name="course_index.html"
    username = request.user.username
    courses = roster_courses()
    dictonary = {'username':username,'courses':courses}

    return render(request, template_name, dictonary)

def prof_perf(request):
    if(not request.user.is_authenticated):
        return redirect('/accounts/login')

    template_name="perf_search.html"
    dictonary={}
    method = request.method
        
    dictonary.update({'method':method})
    if request.method == "POST":
        form = prof_perf_form(request.POST)
        dictonary.update({'form':form})
        post=request.POST
        if 'prof_perf_form' in request.POST:
            #print(form['pname'].value())
            #print(type(form['pname'].value()))
            try:
                prof = Instructor.objects.filter(name=form['pname'].value())
                if not(prof):
                    raise ValueError("No Instructor Found")
                prof_id=prof[0].id
                Teach = roster_prof_classes(prof_id,form['year'].value(),form['sem'].value())
                dictonary.update({'Teach':Teach})
            except ValueError as err:
                dictonary.update({'ClassError':err})
            except DatabaseError as err:
                dictonary.update({'ClassError':err})

            try:
                total = roster_prof_totstud(prof_id,form['year'].value(),form['sem'].value())
                dictonary.update({'tot':total})
            except ValueError as err:
                dictonary.update({'totError':err})
            except DatabaseError as err:
                dictonary.update({'totError':err})

            try:
                if not(prof):
                    raise ValueError("No Instructor Found")
                papers=roster_prof_paper(prof_id)
                if not(papers.exists()):
                    raise ValueError('Querry returned empty results.')
                else:
                    dictonary.update({'papers':papers})
            except ValueError as err:
                dictonary.update({'PaperError':err})
            except DatabaseError as err:
                dictonary.update({'PaperError':err})

            try:
                if not(prof):
                    raise ValueError("No Instructor Found")
                grants=roster_prof_grants(prof_id)
                if not(grants.exists()):
                    raise ValueError('No Grants found')
                else:
                    dictonary.update({'grants':grants})
            except ValueError as err:
                dictonary.update({'GrantError':err})
            except DatabaseError as err:
                dictonary.update({'GrantError':err})

    else:
        form = prof_perf_form()
        dictonary.update({'form':form})

    return render(request, template_name, dictonary)





    
