from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


# Defines a test function for admin_base page

def test(request):
    return render(request, 'hospital/admin_base.html')

# for checking is user is admin


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


# After entering credentials check whether username and password is of admin


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        # It will redirect to the afterlogin page
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/index.html')




def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/adminclick.html')

# for signup/login button for admin

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


# Admin Related Views Start

# Dashboard page view for admin

def admin_dashboard_view(request):
    return render(request, 'hospital/admin_dashboard.html')

# Checking the doctor for admin

def admin_doctor_view(request):
    return render(request, 'hospital/admin_doctor.html')

# patient view for admin

def admin_patient_view(request):
    return render(request, 'hospital/admin_patient.html')

# Appointment view for the admin

def admin_appointment_view(request):
    return render(request, 'hospital/admin_appointment.html')

# Adding patient view by admin

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


# APPOINTMENT START. All appointment function define


def admin_appointment_view(request):
    return render(request, 'hospital/admin_appointment.html')


def admin_view_appointment_view(request):
    appointments = models.Appointment.objects.all().filter(status=True)
    return render(request, 'hospital/admin_view_appointment.html', {'appointments': appointments})


def admin_add_appointment_view(request):
    appointment_form = forms.AppointmentForm()
    mydict = {'appointmentForm': appointment_form, }
    if request.method == 'POST':
        appointment_form = forms.AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.doctorId = request.POST.get('doctorId')
            appointment.patientId = request.POST.get('patientId')
            appointment.doctorName = models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName = models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status = True
            appointment.save()
        return HttpResponseRedirect('admin-view-appointment')
    return render(request, 'hospital/admin_add_appointment.html', context=mydict)


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
