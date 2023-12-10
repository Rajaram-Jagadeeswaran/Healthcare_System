from django import forms
from .models import HealthRecord, Patient

class HealthRecordForm(forms.ModelForm):
    """Form for creating or updating health records."""
    class Meta:
        model = HealthRecord
        fields = ['blood_pressure', 'heart_rate', 'blood_sugar_level', 'cholesterol', 'body_temperature', 'respiratory_rate', 'weight', 'height']

class PatientUpdateForm(forms.ModelForm):
    """Form for updating patient information."""
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 'email', 'contact', 'address']
        