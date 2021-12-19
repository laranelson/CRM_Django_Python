from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=11)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_city(self):
        return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "customer"
# Depois de Criar a class acima é preciso efetuar os passo abaixo 
# 1 - Digitar no terminal >>> python manage.py makemigrations Customer
# 2 - Depois digitar o comando >>> python manage.py migrate
# 3 - Agora é preciso registrar a tabela no arquivo admin.py from .models import Customer