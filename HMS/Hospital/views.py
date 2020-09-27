
from email.headerregistry import Group

from django.contrib.admin import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Define login function
# lower_case

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('login')
    return render(request, 'template/login.html')


# Define available_blood_group function
# lower_case

def available_blood_group(request):
    return render(request, 'template/available_blood_group.html')


# Define blood_bank
# lower_case

def blood_bank(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('blood_bank')
    return render(request, 'template/blood_bank.html')


# Define corona_update
# lower_case

def corona_update(request, user = patients, my_admin_group = doctor):
    form = forms.corona_update()
    if request.method == 'POST':
        form = forms.corona_update(request.POST)
        if form.is_valid():
            user.save()
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('corona_update')
    return render(request, 'hospital/corona_update.html', {'form': form})


# Define donate_blood function
# lower_case

def donate_blood(request):
    return render(request, 'template/donate_blood.html')

# Define footer function
# lower_case

def footer(request):
    return render(request, 'template/footer.html')

# Define home function
# lower_case

def home(request):
    if request.user.is_authenticated:
    return render(request,'template/home.html')

# Define home_slider function
# lower_case

def home_slider(request):
    return render(request, 'template/home_slider.html')

# Define home_base function
# lower_case

def home_base(request):
    return render(request, 'template/home_base.html')

# Define notice function
# lower_case

def notice(request):
    if request.user.is_authenticated:
    return HttpResponseRedirect('notice')
    return render(request, 'template/notice.html')

# Define pharmacy function
# lower_case

def pharmacy(request):
    return render(request, 'template/pharmacy.html')

# Define save_life function
# lower_case

def save_life(request):
    return render(request, 'template/save_life.html')

# Define special_case function
# lower_case

def special_care(request):
    return render(request, 'template/special_case.html')

def about_us_view(request):
    return render(request,'hospital/aboutus.html')
=======
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.shortcuts import render, redirect
=======


from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect



# for showing signup/login button for doctor
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/doctorclick.html')



def doctor_signup_view(request):
    userForm = forms.DoctorUserForm()
    doctorForm = forms.DoctorForm()
    mydict = {'userForm': userForm, 'doctorForm': doctorForm}
    if request.method == 'POST':
        userForm = forms.DoctorUserForm(request.POST)
        doctorForm = forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request, 'hospital/doctorsignup.html', context=mydict)


def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.assignedDoctorId = request.POST.get('assignedDoctorId')
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request, 'hospital/patientsignup.html', context=mydict)


# for checking user is doctor or patient
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()



#for  table in doctor dashboard
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)
=======
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

# Define corona_center


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


# for Ambulance Services


def ambulance(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('ambulance')
    return render(request, 'hospital/ambulance.html')


# for Emergency & ICU Services


def emergency(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('ambulance')
    return render(request, 'hospital/emergency.html')


# for contact us
=======
def corona_update(request, user = patients, my_admin_group = doctor):
    form = forms.corona_center()
    if request.method == 'POST':
        form = forms.corona_center(request.POST)
        if form.is_valid():
            user.save()
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('corona_center')
    return render(request, 'hospital/corona_center.html', {'form': form})



# Define corona_center

def diabetes_update(request, user = patients, my_admin_group = doctor):
    form = forms.diabetes_center()
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
=======
        form = forms.diabetes_center(request.POST)
        if form.is_valid():
            user.save()
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('diabetes_center')
    return render(request, 'hospital/diabetes_center.html', {'form': form})



