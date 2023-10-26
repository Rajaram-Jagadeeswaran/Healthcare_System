from django.http import Http404
from django.shortcuts import render
from .models import Patient, HealthRecord

def patient_list(request):
    user = request.user
    patients = Patient.objects.filter(user=user)
    context = {'patients': patients}
    return render(request, 'patients/patient_list.html', context)

def health_record_list(request, patient_id):
    # context = {
    #     'patient_id': patient_id,
    #     # 'health_records': health_records,
    # }
    # return render(request, 'health_record_list.html', context)
    patient = Patient.objects.get(id=patient_id)
    health_records = HealthRecord.objects.filter(patient=patient)
    return render(request, 'patients/health_record_list.html', {'patient': patient, 'health_records': health_records})