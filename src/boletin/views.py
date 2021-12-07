from django import forms
from django.shortcuts import render
from .forms import Regis_model_form, Contact_Form
from .models import Registrado

# Create your views here.

def index(request): 
    titulo = 'Hi there'
    if request.user.is_authenticated:
        titulo = 'Bienvenido %s' %(request.user)
    form = Regis_model_form(request.POST or None)
    
    context = {
        'titulo' : titulo,
        'formm' : form,
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nombre:
            instance.nombre = 'Persona'
        instance.save()
        
        context = {
            'titulo': 'Gracias %s!' %(instance.nombre)
        }
        
        print(instance)
        print(instance.timestamp)
        
        #form_data = form.cleaned_data
        #form_name = (form_data.get("nombre"))
        #form_email = (form_data.get("email"))
        #Guardar en el modelo
        #save_data = Registrado.objects.create(
        #    nombre=form_name,
        #    email=form_email,
        #)
    return render(request, 'index.html', context)

def contact(request):
    titulo = 'Hi, Welcome to contact View'
    form = Contact_Form(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data:
            print(key)
            print(form.cleaned_data.get(key))
    context = {
        'form_contact': form,
        'titulo': titulo
    }
    return render(request, 'forms.html', context)
