from django import forms
from django.forms import fields
from .models import Registrado

#Creando nuestros formularios
class Reg_Form(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    
#Creando formulario con nuestro modelo
class Regis_model_form(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ['nombre', 'email']