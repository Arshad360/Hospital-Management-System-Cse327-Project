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
