from django.shortcuts import render
from.models import Pharmacy

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('login')
    return render(request, 'Template/login.html')

def pharmacy(request):

    return render (request,'Template/Pharmacy.html',{'Pharmacy':Pharmacy})

