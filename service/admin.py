from django.contrib import admin
from .models import Service

# Essa class server para listar os campos da tabela Service na parte de gerenciamento do Django
@admin.register(Service)# isso é um decorador
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "service_name", "surname"]

    # Nelson Lara