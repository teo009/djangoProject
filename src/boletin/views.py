from django import forms
from django.shortcuts import render
from .forms import Reg_Form

# Create your views here.

def index(request): 
    form = Reg_Form(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data.get("nombre"))
        print(form.data.get("edad"))
    context = {
        'formm' : form,
    }
    return render(request, 'index.html', context)
