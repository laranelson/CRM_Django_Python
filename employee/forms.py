from django import forms
from django.forms import fields
from .models import Employee


class EmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(
                                label="Nome",
                                error_messages={"max_length":"Nome não pode ultrapassar 30 caracteres."}
                                )
    position = forms.CharField(
                                label="Cargo",
                                error_messages={"max_length":"Cargo não pode ultrapassar 30 caracteres."}
                                )
    
    class Meta():
        model = Employee
        fields = ("employee_name", "position") 

