from django import forms
from django.forms import fields
from django.forms.widgets import DateInput

from customer.models import Customer  
from service.models import Service
from employee.models import Employee

from .models import Attendance


class DateInput(forms.DateInput):
    input_type = "date"


class AttendanceForm(forms.ModelForm):


    customer = forms.ModelChoiceField(label="Cliente", queryset=Customer.objects.all(), to_field_name='id', empty_label='Selecione o cliente')

    service = forms.ModelChoiceField(label="Serviço", queryset=Service.objects.all(), to_field_name='id', empty_label='Selecione o serviço')

    employee = forms.ModelChoiceField(label="Funcionário", queryset=Employee.objects.all(), to_field_name='id', empty_label='Selecione o funcionário')

    attendance_date = forms.DateField(label="Data do Atendimento", widget=DateInput())

    attendance_description = forms.CharField(label="Descrição")


    class Meta():
        model = Attendance
        fields = (
            "customer",
            "service",
            "employee",
            "attendance_date",
            "attendance_description"
            
        ) 

    
    



