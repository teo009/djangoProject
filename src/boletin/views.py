from django import forms
from django.shortcuts import render
from .forms import Reg_Form

# Create your views here.

def index(request): 
    form = Reg_Form()
    context = {
        'formm' : form,
    }
    return render(request, 'index.html', context)
