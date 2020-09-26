from django.db import models

from django.contrib.auth.models import User

# Create your models here

# All the departments

departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]

# Defines of the Appointment Class

class Appointment(models.Model):
    # Gets the patientId
    patientId models.PositiveIntegerField(null=True)
    # Gets the doctorId
    doctorId = models.PositiveIntegerField(null=True)
    # Gets the patientName
    patientName = models.CharField(max_length=40, null=True)
    # Gets the doctorName
    doctorName = models.CharField(max_length=40, null=True)
    # Gets the appointmentDate
    appointmentDate = models.DateField(auto_now=True)
    # Gets the description
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
