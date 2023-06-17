from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Digimon



def index(request):
  digimons =  Digimon.objects.all() #consulta a la base de datos 

  context = {
    'digis': digimons
  }

  return render(request, 'index.html', context)
# Create your views here.

@csrf_exempt
def create(request):
  params = request.POST  # no guarda en db
  digi = Digimon() # no guarda en db
  digi.name = params ["name"] # no guarda en db
  digi.level = params ["level"] # no guarda en db
  digi.img = params ["img"] # no guarda en db
  digi.save() # guarda en la base de datos 

  return HttpResponse(status = 200)
                  
  
  #Las peticiones que se puede realizar en la web
  #GET verbo
  #POST verbo
  #PUT verbo
  #DELETE verbo
  