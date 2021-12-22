# VOU CRIAR TUDO DO ZERO
from django.urls import path
from .views import (
                    ServiceListView, 
                    ServiceCreateView, 
                    ServiceUpdateView, 
                    ServiceDeleteView
)

app_name = "service"

urlpatterns = [
    path("list/", ServiceListView.as_view(), name="service-list"),
    path("", ServiceCreateView.as_view(), name="service-create"),
    path("<int:id>/", ServiceUpdateView.as_view(), name="service-update"),
    path("<int:id>/delete/", ServiceDeleteView.as_view(), name="service-delete")
]