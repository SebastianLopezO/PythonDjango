from django.shortcuts import render
from datetime import datetime
from academico.models import Facultad

# Create your views here.

def facultades(request) :
    facultad = Facultad.objects.all()
    actual = datetime.now()
    # contexto
    context = {"facultad":facultad, "actual":actual}
    return render(request, "facultades.html", context)
