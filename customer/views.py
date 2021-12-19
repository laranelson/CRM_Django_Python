from django.shortcuts import get_object_or_404, render
from django.views.generic import (
                                    ListView, 
                                    CreateView, 
                                    UpdateView, 
                                    DeleteView
)
from .models import Customer
from .forms import CustomeForm
from django.urls import reverse
from django.shortcuts import get_list_or_404
from django.db.models import Q

class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 5
    model = Customer
    #queryset = Customer.objects.all()
    
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                                                    Q(first_name__icontains=name) |
                                                    Q(last_name__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomeForm

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")

class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomeForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    # validar o formulário | validation the form
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")

class CustomerDeleteView(DeleteView):
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def get_success_url(self):
        return reverse("customer:customer-list")
   
# Create your views here.