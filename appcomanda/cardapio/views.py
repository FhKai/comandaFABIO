from django.shortcuts import render
from django.http import HttpResponse
from .models import TipoProduto, ProdutoCardapio

def cardapio(request, slug):
    return HttpResponse (slug)
