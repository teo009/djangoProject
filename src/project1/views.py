#Views pero fuera de la app de django, para configurar barra de navegación

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def galery(request): 
    return render(request, 'galery.html', {})