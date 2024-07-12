from django.urls import path
from . import views

urlpatterns = [
    path('officers/', views.officer_list, name='officer_list'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('reports/', views.report_list, name='report_list'),
]
