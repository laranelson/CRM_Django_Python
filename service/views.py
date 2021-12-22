from django.shortcuts import get_object_or_404, render
from django.views.generic import (
                                    ListView, 
                                    CreateView, 
                                    UpdateView, 
                                    DeleteView
)
from .models import Service
from .forms import ServiceForm
from django.urls import reverse
from django.shortcuts import get_list_or_404
from django.db.models import Q

class ServiceListView(ListView):
    template_name = "service/service_list.html"
    paginate_by = 5
    model = Service
    #queryset = Service.objects.all()
    
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                                                    Q(service_name__icontains=name) |
                                                    Q(surname__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class ServiceCreateView(CreateView):
    template_name = "service/service.html"
    form_class = ServiceForm

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("service:service-list")

class ServiceUpdateView(UpdateView):
    template_name = "service/service.html"
    form_class = ServiceForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Service, id=id)

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("service:service-list")

class ServiceDeleteView(DeleteView):
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Service, id=id)

    def get_success_url(self):
        return reverse("service:service-list")
   
