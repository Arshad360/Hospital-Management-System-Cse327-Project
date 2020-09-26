from django import forms
from django.contrib.auth.models import User
from . import models


# Class for admin sign up form


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# Class for Appointment form


class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),
                                      empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),
                                       empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


# Class for contact us form


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
