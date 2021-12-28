from django.contrib import admin
from .models import Employee

# Essa class server para listar os campos da tabela Employee na parte de gerenciamento do Django
@admin.register(Employee)# isso é um decorador
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "employee_name", "position"]

    # Nelson Lara