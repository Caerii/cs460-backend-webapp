from .models import *
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min

#import later on


def roster_prof_name(): 
    """get query list of professors by name """
    return Instructor.objects.order_by('name')

def roster_prof_dept(dept:str):
    """get query list of professors by department"""
     # dept represents department name as a string.
    #if any department use '*'
    return Instructor.objects.order_by('Dept_Name').filter(dept_name=dept)

def roster_prof_salary():
    """get query list of professors by salary"""
    return Instructor.objects.order_by('Salary')

# departmental min, max and average salaries

def roster_department():
    """Returns a query of avaliable departments"""
    return Department.objects.order_by('name')

def dept_Instructors(dept:str):
    """Returns querryset of departmental instructors"""
    return Instructor.objects.filter(dept_name = dept)

# professor performance functions 
def Instructor_taught(Inst_name:str,acad_year:int,semester):
    """gives list of taught courses in a semsester and academic year."""
    inst_ID = Instructor.objects.filter(name = Inst_name)[0]
    return Teaches.objects.filter(ID = inst_ID).filter(year = acad_year).filter(semester = semester)


    
