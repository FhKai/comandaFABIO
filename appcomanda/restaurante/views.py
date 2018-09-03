from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurante

def lista_de_restaurantes(request):
    restaurantes = Restaurante.objects.all().order_by('nome')
    return render(request, 'restaurante/restaurantes.html', {'restaurantes':restaurantes})

def detalhes_restaurante(request, slug):
    restaurante = Restaurante.objects.get(slug=slug)
    return render(request, 'restaurante/detalhes_restaurante.html', {'restaurante':restaurante})
