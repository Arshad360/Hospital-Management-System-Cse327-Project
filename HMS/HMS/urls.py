"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/2.0/topics/http/urls/
=======
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

from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from HMS.Hospital.views import *



urlpatterns = {
    path('admin/', admin.site.urls),
    path('available_blood_group', available_blood_group),
    path('blood_bank', blood_bank),
    path('corona_update', corona_update),
    path('donate_blood', donate_blood),
    path('footer', footer),
    path('home', home),
    path('home_base', home_base),
    path('home_slider', home_slider),
    path('login', login),
    path('notice',notice),
    path('special_care',special_care),
    path('save_life', save_life),




}


=======
from django.contrib import admin
from django.urls import path


from HMS.Hospital import views
from HMS.Hospital.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path

from HMS.Hospital import views
from HMS.Hospital.views import *
from django.contrib.auth.views import LoginView, LogoutView


# FOR DOCTOR RELATED URLS
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
=======
from HMS.Hospital.views import *
from django.contrib.auth.views import LoginView, LogoutView

# FOR ADMIN RELATED URLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name=''),
    path('test/', test, name='test'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'), name='logout'),
    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
    path('admin-doctor', admin_doctor_view, name='admin-doctor'),
    path('admin-patient', admin_patient_view, name='admin-patient'),
    path('admin-appointment', admin_appointment_view, name='admin-appointment'),
    path('contactus', contactus_view),

]


