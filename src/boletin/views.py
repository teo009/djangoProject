from django import forms
from django.shortcuts import render
from .forms import Reg_Form
from .models import Registrado

# Create your views here.

def index(request): 
    form = Reg_Form(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        form_name = (form_data.get("nombre"))
        form_email = (form_data.get("email"))
        #Guardar en el modelo
        save_data = Registrado.objects.create(
            nombre=form_name,
            email=form_email,
        )
    context = {
        'formm' : form,
    }
    return render(request, 'index.html', context)
