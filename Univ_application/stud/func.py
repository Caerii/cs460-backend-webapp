from .models import *

def section_by_year(dept, sem, yr):
    """get query list of sections in a given year and semester """
    return Section.objects.filter(year = yr, semester = sem, course__dept_name = dept)