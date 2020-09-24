from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('')
    return render(request, 'hospital/index.html')
