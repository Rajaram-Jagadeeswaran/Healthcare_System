from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patientList, name='patient_list'),
    path('health_records/<int:user_id>/', views.healthRecordList, name='health_record_list'),
    path('patients/<int:user_id>/', views.healthRecordList, name='health_record'),
    path('patients/update/<int:user_id>/', views.updatePatient, name='update_patient'),
    path('patients/createhealth_record/<int:user_id>/', views.healthRecordCreate, name='health_record_create'),
    path('patients/updatehealth_record/<int:user_id>/<int:record_id>/', views.healthRecordUpdate, name='health_record_update'),
    path('patients/deletehealth_record/<int:user_id>/<int:record_id>/', views.healthRecordDelete, name='health_record_delete'),
]