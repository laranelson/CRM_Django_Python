from django.contrib import admin
from .models import Customer

# Essa class server para listar os campos da tabela Customer na parte de gerenciaento do Django
@admin.register(Customer)# isso é um decorador
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email"]

    # Nelson Lara

# Register your models here.
