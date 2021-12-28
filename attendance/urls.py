# VOU CRIAR TUDO DO ZERO
from django.urls import path
from .views import (
                    AttendanceListView, 
                    AttendanceCreateView, 
                    AttendanceUpdateView, 
                    AttendanceDeleteView
)

app_name = "attendance"

urlpatterns = [
    path("list/", AttendanceListView.as_view(), name="attendance-list"),
    path("", AttendanceCreateView.as_view(), name="attendance-create"),
    path("<int:id>/", AttendanceUpdateView.as_view(), name="attendance-update"),
    path("<int:id>/delete/", AttendanceDeleteView.as_view(), name="attendance-delete")
]