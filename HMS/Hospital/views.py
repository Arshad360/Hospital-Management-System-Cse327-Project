from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render, redirect
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


# for signup/login button for admin

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/adminclick.html')


def admin_signup_view(request):
    form = forms.AdminSigupForm()
    if request.method == 'POST':
        form = forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request, 'hospital/adminsignup.html', {'form': form})


def admin_dashboard_view(request):
    return render(request, 'hospital/admin_dashboard.html')


def admin_doctor_view(request):
    return render(request, 'hospital/admin_doctor.html')


def admin_patient_view(request):
    return render(request, 'hospital/admin_patient.html')


def admin_appointment_view(request):
    return render(request, 'hospital/admin_appointment.html')


def admin_add_patient_view(request):
    user_form = forms.PatientUserForm()
    patient_form = forms.PatientForm()
    my_dict = {'user_form': user_form, 'patient_form': patient_form}
    if request.method == 'POST':
        user_form = forms.PatientUserForm(request.POST)
        patient_form = forms.PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            patient = patient_form.save(commit=False)
            patient.user = user
            patient.status = True
            patient.assignedDoctorId = request.POST.get('assignedDoctorId')
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-patient')
    return render(request, 'hospital/admin_add_patient.html', context=my_dict)

# after successful login


def afterlogin_view(request):
    return render(request, 'hospital/admin-dashboard.html')


# for contact us


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message,
                      EMAIL_HOST_USER, ['arshadrakib2@gmail.com'],
                      fail_silently=False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form': sub})
