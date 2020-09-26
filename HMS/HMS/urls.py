"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from HMS.Hospital.views import *
from django.contrib.auth.views import LoginView, LogoutView

# FOR ADMIN RELATED URLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name=''),
    path('test/', test, name='test'),
    path('adminsignup', admin_signup_view),
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'), name='logout'),
    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
    path('admin-doctor', admin_doctor_view, name='admin-doctor'),
    path('admin-patient', admin_patient_view, name='admin-patient'),
    path('admin-add-patient', admin_add_patient_view, name='admin-add-patient'),
    path('admin-appointment', admin_appointment_view, name='admin-appointment'),
    path('adminclick', adminclick_view),
    path('afterlogin', afterlogin_view, name='afterlogin'),
    path('contactus', contactus_view),

]
