from django.db import models
from django.urls import reverse


class Employee(models.Model):
    employee_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.employee_name} {self.position}"

    def get_absolute_url(self):
        return reverse("employee:employee-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("employee:employee-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "employee"
        
# Depois de Criar a class acima é preciso efetuar os passo abaixo 
# 1 - Digitar no terminal >>> python manage.py makemigrations employee
# 2 - Depois digitar o comando >>> python manage.py migrate
# 3 - Agora é preciso registrar a tabela no arquivo admin.py from .models import employee