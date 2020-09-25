from django.shortcuts import render
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


def test(request):
    return render(request, 'hospital/admin_base.html')


# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/index.html')


def admin_dashboard_view(request):
    return render(request, 'hospital/admin_dashboard.html')


def admin_doctor_view(request):
    return render(request, 'hospital/admin_doctor.html')


def admin_patient_view(request):
    return render(request, 'hospital/admin_patient.html')


def admin_appointment_view(request):
    return render(request, 'hospital/admin_appointment.html')
