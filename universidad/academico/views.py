from django.shortcuts import render
from datetime import datetime
from academico.models import *

# Create your views here.

def main(request) :
    actual = datetime.now()
    # contexto
    context = {"actual":actual}
    return render(request, "main.html", context)
    
def SelectModel(model):
    model = model.lower()
    if(model=="facultad"):
        return Facultad
    elif(model=="carrera"):
        return Carrera
    elif(model=="docente"):
        return Docente
    elif(model=="curso"):
        return Curso

def eliminar(request) :
    user =  request.GET.get('id')
    model =  SelectModel(request.GET.get('model'))
    data = model.objects.values_list().get(id=user)
    schema = model._meta.fields
    # contexto
    context = {"id":user, "data":data, "schema":schema, "action":"Eliminar"}
    return render(request, "actions.html", context)
    
def modificar(request) :
    user =  request.GET.get('id')
    model =  SelectModel(request.GET.get('model'))
    data = model.objects.values_list().get(id=user)
    schema = model._meta.fields
    # contexto
    context = {"id":user, "data":data, "schema":schema, "action":"Modificar"}
    return render(request, "actions.html", context)    

def facultades(request) :
    data = Facultad.objects.values_list()
    schema = Facultad._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema, "model":"Facultad"}
    return render(request, "crud.html", context)
    
def carreras(request) :
    data = Carrera.objects.values_list()
    schema = Carrera._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema, "model":"Carrera"}
    return render(request, "crud.html", context)
    
def cursos(request) :
    data = Curso.objects.values_list()
    schema = Curso._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema, "model":"Curso"}
    return render(request, "crud.html", context)

def docentes(request) :
    data = Docente.objects.values_list()
    schema = Docente._meta.fields
    actual = datetime.now()
    # contexto
    context = {"data":data, "actual":actual,"schema":schema, "model":"Docente"}
    return render(request, "crud.html", context)
    
