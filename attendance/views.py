from django.shortcuts import get_object_or_404, render
from django.views.generic import (
                                    ListView, 
                                    CreateView, 
                                    UpdateView, 
                                    DeleteView
)
from .models import Attendance
from .forms import AttendanceForm
from django.urls import reverse
from django.shortcuts import get_list_or_404
from django.db.models import Q

class AttendanceListView(ListView):
    template_name = "attendance/attendance_list.html"
    paginate_by = 5
    model = Attendance
    #queryset = Attendance.objects.all()
    
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                                                    Q(customer_id__icontains=name) |
                                                    Q(service_id__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class AttendanceCreateView(CreateView):
    template_name = "attendance/attendance.html"
    form_class = AttendanceForm

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("attendance:attendance-list")

class AttendanceUpdateView(UpdateView):
    template_name = "attendance/attendance.html"
    form_class = AttendanceForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Attendance, id=id)

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("attendance:attendance-list")

class AttendanceDeleteView(DeleteView):
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Attendance, id=id)

    def get_success_url(self):
        return reverse("attendance:attendance-list")
   
