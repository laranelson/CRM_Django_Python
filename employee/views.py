from django.shortcuts import get_object_or_404, render
from django.views.generic import (
                                    ListView, 
                                    CreateView, 
                                    UpdateView, 
                                    DeleteView
)
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse
from django.shortcuts import get_list_or_404
from django.db.models import Q

class EmployeeListView(ListView):
    template_name = "employee/employee_list.html"
    paginate_by = 5
    model = Employee
    #queryset = Employee.objects.all()
    
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                                                    Q(employee_name__icontains=name) |
                                                    Q(position__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class EmployeeCreateView(CreateView):
    template_name = "employee/employee.html"
    form_class = EmployeeForm

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("employee:employee-list")

class EmployeeUpdateView(UpdateView):
    template_name = "employee/employee.html"
    form_class = EmployeeForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id)

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("employee:employee-list")

class EmployeeDeleteView(DeleteView):
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id)

    def get_success_url(self):
        return reverse("employee:employee-list")