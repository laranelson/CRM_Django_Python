from django import forms
from django.forms import fields
from .models import Service


class ServiceForm(forms.ModelForm):
    service_name = forms.CharField(
                                label="Serviço",
                                error_messages={"max_length":"Nome não pode ultrapassar 30 caracteres."}
                                )
    surname = forms.CharField(
                                label="Apelido",
                                error_messages={"max_length":"Apelido não pode ultrapassar 30 caracteres."}
                                )
    
    class Meta():
        model = Service
        fields = ("service_name", "surname") 

