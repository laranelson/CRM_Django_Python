from django.db import models
from django.urls import reverse
from customer.models import Customer
from service.models import Service
from employee.models import Employee


class Attendance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    attendance_date = models.DateField()
    attendance_description = models.TextField(max_length=1000)
    
   
    
    def get_absolute_url(self):
        return reverse("attendance:attendance-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("attendance:attendance-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "attendance"
