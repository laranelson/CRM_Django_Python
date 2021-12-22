from django.db import models
from django.urls import reverse


class Service(models.Model):
    service_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.service_name} {self.surname}"

    def get_absolute_url(self):
        return reverse("service:service-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("service:service-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "service"
        
# Depois de Criar a class acima é preciso efetuar os passo abaixo 
# 1 - Digitar no terminal >>> python manage.py makemigrations service
# 2 - Depois digitar o comando >>> python manage.py migrate
# 3 - Agora é preciso registrar a tabela no arquivo admin.py from .models import service