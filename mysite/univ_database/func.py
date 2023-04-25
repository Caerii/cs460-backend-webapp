from .models import *
from django.db import connection
from collections import namedtuple
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min

#import later on


def roster_prof(sort_term): 
    """get query list of professors by name """
    return Instructor.objects.order_by(sort_term)

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

def roster_courses():
    """gives list of course"""
    return Course.objects.order_by('dept_name')

def roster_prof_classes(prof_id:int,year:int,semester:int):
    """Querrying Professor classes by year and semester"""
    with connection.cursor() as cursor:
        cursor.execute("""select te.course_id, te.sec_id
                        from teaches te
                        where te.teacher_id = %s and te.year = %s and te.semester = %s""" ,(str(prof_id),str(year),str(semester)))
        result = namedtuplefetchall(cursor)
    return result

def roster_prof_paper(prof_id:int):
    """Querying Professor Papers from id"""
    return Papers.objects.filter(researcher_id=prof_id)

def roster_prof_grants(prof_id:int):
    """Querying Professor Grants for research and related research"""
    return FundGrants.objects.filter(receiver=prof_id)

def namedtuplefetchall(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]