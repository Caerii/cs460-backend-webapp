from .models import *

#import later on or, copy and past

#proofesor roster

def roster_prof_name(page): 
    return Instructor.objects.order_by('Name')

def roster_prof_dept(page, dept:str): # dept represents department name as a string
    return Instructor.objects.order_by('Dept_Name').filter(Instructor.dept_name==dept)

def roster_prof_salary(page):
    return Instructor.objects.order_by('Salary')
