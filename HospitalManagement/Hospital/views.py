from django.shortcuts import render
from django.shortcuts import render, redirect, reverse

from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('')
    return render(request, 'index.html')