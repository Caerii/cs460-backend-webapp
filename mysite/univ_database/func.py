from .models import *
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min

#import later on

#profesor roster 
def roster_prof_name(): 
    return Instructor.objects.order_by('Name')

def roster_prof_dept(dept:str): # dept represents department name as a string.
    #if any department use '*'
    return Instructor.objects.order_by('Dept_Name').filter(dept_name=dept)

def roster_prof_salary(page):
    return Instructor.objects.order_by('Salary')

# departmental min, max and average salaries

def dept_salary_stats(dept:str):
    max_sal = Instructor.objects.filter(dept_name = dept).aggregate(Max('salary'))[0]
    min_sal = Instructor.objects.filter(dept_name = dept).aggregate(Min('salary'))[0]
    avg_sal = Instructor.objects.filter(dept_name = dept).aggregate(Avg('salary'))[0]
    return [max_sal,min_sal,avg_sal]


# professor performance functions 
# gives list of taught courses in a semsester and academic year.
def Instructor_taught(Inst_name:str,acad_year:int,semester):
    inst_ID = Instructor.objects.filter(name = Inst_name)[:1]
    return Teaches.objects.filter(ID = inst_ID).filter(year = acad_year).filter(semester = semester)


    
