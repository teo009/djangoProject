#Views pero fuera de la app de django, para configurar barra de navegación

from django.shortcuts import render

# Create your views here.

def galery(request): 
    return render(request, 'galery.html', {})