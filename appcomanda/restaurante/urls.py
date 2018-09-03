from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from cardapio import views as views_cardapio

urlpatterns = [
    path('', views.lista_de_restaurantes, name='lista'),
    url(r'^(?P<slug>[\w-]+)/$', views.detalhes_restaurante, name='detalhes'),
]
