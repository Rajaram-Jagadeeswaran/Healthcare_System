from django import forms
from.models import HealthRecord
from .models import Patient

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        exclude = ['user']
        fields = ['user', 'blood_pressure', 'heart_rate', 'blood_sugar_level', 'cholesterol', 'body_temperature', 'respiratory_rate', 'weight', 'height']
        
class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 'email', 'contact', 'address']