from django.shortcuts import render
from datetime import datetime
from academico.models import Facultad

# Create your views here.

def facultades(request) :
    facultad = Facultad.objects.values_list()
    schema = Facultad._meta.fields
    actual = datetime.now()
    # contexto
    context = {"facultad":facultad, "actual":actual,"schema":schema}
    return render(request, "facultades.html", context)
