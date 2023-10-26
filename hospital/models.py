from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, default='Null')
    email = models.EmailField(default='Null')
    contact = models.CharField(max_length=10, default='Null')
    address = models.CharField(max_length=100, default= 'Null')
    
    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)
    blood_sugar_level = models.CharField(max_length=20),
    cholesterol = models.FloatField(default=0)
    body_temperature = models.FloatField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    
    def __str__(self):
        return f"Record - ({self.patient})"