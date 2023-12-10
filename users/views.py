"""
Module: users.views
Description: Contains views related to user management.
"""

from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
from hospital.models import Patient, HealthRecord

def sign_up(request):
    """
    View for user sign-up.

    If the request method is POST, it processes the form and redirects to
    the sign-in page upon successful registration. If the request method is
    GET, it renders the sign-up form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account has been successfully created for {}.'.format(username))
            return redirect('/signin')
    elif request.method == "GET":
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
