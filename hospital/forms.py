from django import forms
from.models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        exclude = ['user']
        fields = ['user', 'blood_pressure', 'heart_rate', 'blood_sugar_level', 'cholesterol', 'body_temperature', 'respiratory_rate', 'weight', 'height']