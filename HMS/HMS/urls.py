"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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



