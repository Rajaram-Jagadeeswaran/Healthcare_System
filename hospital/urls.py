"""URL configuration for the hospital app"""
from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('health_records/<int:user_id>/', views.health_record_list, name='health_record_list'),
    path('patients/<int:user_id>/', views.health_record_list, name='health_record'),
    path('patients/update/<int:user_id>/', views.update_patient, name='update_patient'),
    path('patients/createhealth_record/<int:user_id>/', views.health_record_create, name='health_record_create'),
    path('patients/updatehealth_record/<int:user_id>/<int:record_id>/', views.health_record_update, name='health_record_update'),
    path('patients/deletehealth_record/<int:user_id>/<int:record_id>/', views.health_record_delete, name='health_record_delete'),
    path('healthChart/<int:user_id>/', views.health_chart, name='health_chart'),
]