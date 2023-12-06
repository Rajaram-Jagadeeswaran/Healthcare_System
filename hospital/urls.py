from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('health_records/<int:user_id>/', views.health_record_list, name='health_record_list'),
    path('patients/<int:user_id>/', views.health_record_list, name='health_record'),
    path('patients/createhealth_record/<int:user_id>/', views.health_record_create, name='health_record_create'),
]