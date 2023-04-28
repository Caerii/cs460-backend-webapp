from .models import *
from django.db import connection
from collections import namedtuple

def sections_by_prof(sem, name):

    instr = Instructor.objects.get(name = name)
    id = (int)(instr.id)
    with connection.cursor() as cursor:
            cursor.execute("""select c.course_id, c.sec_id, c.semester, c.year, c.building, c.room, c.capacity, s.class_size
                              from section c,
                              	(select ta.course_id, ta.sec_id, ta.semester, ta.year, Count(*) as class_size
                              	from takes ta, teaches t
                              	where ta.course_id = t.course_id and ta.sec_id = t.sec_id and ta.semester = t.semester and ta.year = t.year and t.teacher_id = %s
                              	group by course_id, sec_id, semester, year) s
                              where c.course_id = s.course_id and c.sec_id = s.sec_id and c.semester = s.semester and c.year = s.year and s.semester = %s""", (id, sem))
            result = namedtuplefetchall(cursor)
    return result

def students_by_section(cour, sec, sem, yr):

    with connection.cursor() as cursor:
            cursor.execute("""select s.id, s.name, s.dept_name, s.tot_cred
                              from student s, takes t
                              where s.id = t.student_id and t.course_id = %s and t.sec_id = %s and t.semester = %s and t.year = %s""", (cour, sec, sem, yr))
            result = namedtuplefetchall(cursor)
    return result

def namedtuplefetchall(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]