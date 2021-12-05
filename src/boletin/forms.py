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
        
    #Creando nuestras propias validaciones
    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        #Validación .edu en los emails
        email_base, email_provider = email_field.split('@')
        email_domain, email_extension = email_provider.split('.')
        if not email_extension == 'edu':
            raise forms.ValidationError('Por favor, utiliza un correo con la extención ".edu"')
        return email_field
    
    def clean_nombre(self):
        nombre_field = self.cleaned_data.get('nombre')
        #Validaciones
        return nombre_field