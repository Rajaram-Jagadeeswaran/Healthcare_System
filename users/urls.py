"""
URL patterns for the users app.
"""

from django.urls import path
from . import views

app_name = 'users'  # Updated to UPPER_CASE naming style

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
]