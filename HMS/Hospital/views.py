
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

# Define corona_center

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
        form = forms.diabetes_center(request.POST)
        if form.is_valid():
            user.save()
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('diabetes_center')
    return render(request, 'hospital/diabetes_center.html', {'form': form})


