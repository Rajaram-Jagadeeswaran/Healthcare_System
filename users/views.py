from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
from hospital.models import Patient, HealthRecord

def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            un = form.cleaned_data.get('username')

            # Creating associated Patient instance for the new user
            patient = Patient.objects.create(user=user, name=un)

            messages.success(request, 'Account has been successfully created for {}.'.format(un))
            return redirect('/signin')
    elif request.method == "GET":
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
