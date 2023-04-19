from .models import *
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min

def section_by_year(sem, yr):
    """get query list of sections in a given year and semester """
    return Section.objects.filter(year = yr, semester = sem)