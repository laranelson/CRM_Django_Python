from django import forms
from django.forms import fields
from django.forms.widgets import DateInput    
from .models import Customer


class DateInput(forms.DateInput):
    input_type = "date"

class CustomeForm(forms.ModelForm):
    first_name = forms.CharField(
                                label="Nome",
                                error_messages={"max_length":"Nome não pode ultrapassar 30 caracteres."}
                                )
    last_name = forms.CharField(
                                label="Sobrenome",
                                error_messages={"max_length":"Sobrenome não pode ultrapassar 30 caracteres."}
                                )
    email = forms.EmailField(
                                label="E-mail",
                                error_messages={"invalid":"E-mail inválido, tente novamente."}
                                )
    birth_date = forms.DateField(label="Data de Nascimeto", widget=DateInput())
    area_code = forms.RegexField(
                                label="DDD",
                                regex=r"^\+?1?[0-9]{2}$",
                                error_messages={"invalid": "DDD inválido"}
                                )
    phone_number = forms.RegexField(
                                label="Telefone",
                                regex=r"^\+?1?[0-9]{9,15}$",
                                error_messages={"invalid": "\Telefone inválido"}
                                )
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta():
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        ) 

