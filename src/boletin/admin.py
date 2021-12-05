from django.contrib import admin

# Register your models here.

from .models import Registrado
from .forms import Regis_model_form

class AdminRegistrado(admin.ModelAdmin): 
    list_display = ["__str__", "nombre", "timestamp"]
    form = Regis_model_form
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    #class Meta: 
    #    model = Registrado

admin.site.register(Registrado, AdminRegistrado)
