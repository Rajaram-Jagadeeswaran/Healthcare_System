from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('health_records/<int:patient_id>/', views.health_record_list, name='health_record_list'),
    path('patients/<int:patient_id>/', views.health_record_list, name='health_record'),
]