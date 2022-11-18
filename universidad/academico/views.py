from django.shortcuts import render
from datetime import datetime
from academico.models import *

# Create your views here.

def main(request) :
    actual = datetime.now()
    # contexto
    context = {"actual":actual}
    return render(request, "main.html", context)

def facultades(request) :
    data = Facultad.objects.values_list()
    schema = Facultad._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema}
    return render(request, "crud.html", context)
    
def carreras(request) :
    data = Carrera.objects.values_list()
    schema = Carrera._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema}
    return render(request, "crud.html", context)
    
def cursos(request) :
    data = Curso.objects.values_list()
    schema = Curso._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema}
    return render(request, "crud.html", context)

def docentes(request) :
    data = Docente.objects.values_list()
    schema = Docente._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema}
    return render(request, "crud.html", context)
    
