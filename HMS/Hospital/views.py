from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Pharmacy


# Define login function
# lower_case

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('login')
    return render(request, 'Template/login.html')


# Define available_blood_group function
# lower_case

def login(request):
    return render(request, 'Template/available_blood_group.html')


# Define blood_bank
# lower_case

def login(request):
    return render(request, 'Template/blood_bank.html')


# Define corona_update
# lower_case

def login(request):
    return render(request, 'Template/corona_update.html')


# Define donate_blood function
# lower_case

def login(request):
    return render(request, 'Template/donate_blood.html')


# Define footer function
# lower_case

def login(request):
    return render(request, 'Template/footer.html')


# Define home function
# lower_case

def login(request):
    return render(request, 'Template/home.html')


# Define home_slider function
# lower_case

def login(request):
    return render(request, 'Template/home_slider.html')


# Define home_base function
# lower_case

def login(request):
    return render(request, 'Template/home_base.html')


# Define navbar function
# lower_case

def login(request):
    return render(request, 'Template/navbar.html')


# Define notice function
# lower_case

def login(request):
    return render(request, 'Template/notice.html')


# Define pharmacy function
# lower_case

def login(request):
    return render(request, 'Template/pharmacy.html')


# Define save_life function
# lower_case

def login(request):
    return render(request, 'Template/save_life.html')


# Define special_case function
# lower_case

def login(request):
    return render(request, 'Template/special_case.html')
