from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Patient, HealthRecord

from .forms import HealthRecordForm 

def home(request):
   return render(request, 'patients/index.html')

def patient_list(request):
    user = request.user
    patients = Patient.objects.filter(user=user)
    context = {'patients': patients}
    return render(request, 'patients/patient_list.html', context)

def health_record_list(request, user_id):
    user = request.user
    health_records = HealthRecord.objects.filter(user=user)
    print(user)
    print(health_records)
    return render(request, 'patients/health_record_list.html', {'user': user, 'health_records': health_records})

def new(request):
    return render(request, 'patients/health_record_create_form.html', {'form': HealthRecordForm})
   
def health_record_create(request, user_id):
    user = request.user
    health_records = HealthRecord.objects.filter(user=user)
    print(user)
    print(health_records)

    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            health_record = form.save(commit=False)
            health_record.user = user
            health_record.save()
            return redirect('hospital:health_record_list', user_id=user.id)
    else:
        form = HealthRecordForm(initial={'user': user.username})

    return render(request, 'patients/health_record_create_form.html', {'form': form, 'user': user})