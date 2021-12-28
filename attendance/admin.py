from django.contrib import admin
from .models import Attendance

# Essa class server para listar os campos da tabela Attendance na parte de gerenciamento do Django
@admin.register(Attendance)# isso é um decorador
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_id", "service_id", "employee_id"]

    # Nelson Lara

