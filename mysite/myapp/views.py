from django.shortcuts import render
import mysql.connector

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Instructor 

def index(request):
  
  template = loader.get_template('myapp/form.html')
  context = { }

  return HttpResponse(template.render(context, request))


def show(request):
  
  amount=request.POST['amount']
  print(amount)

  data = Instructor.objects.filter(salary__gt=amount)
  for r in data:
     print(r)
  template = loader.get_template('myapp/table.html')
  context = {
        'rows': data,
    }

  return HttpResponse(template.render(context, request))
