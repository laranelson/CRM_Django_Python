# VOU CRIAR TUDO DO ZERO
from django.urls import path
from .views import (
                    EmployeeListView, 
                    EmployeeCreateView, 
                    EmployeeUpdateView, 
                    EmployeeDeleteView
)

app_name = "employee"

urlpatterns = [
    path("list/", EmployeeListView.as_view(), name="employee-list"),
    path("", EmployeeCreateView.as_view(), name="employee-create"),
    path("<int:id>/", EmployeeUpdateView.as_view(), name="employee-update"),
    path("<int:id>/delete/", EmployeeDeleteView.as_view(), name="employee-delete")
]