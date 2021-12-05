from django import forms

#Creando nuestros formularios
class Reg_Form(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()