from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Patient


def index(request):
    latest_patient_list = Patient.objects.all()[:5]
    context = {'latest_patient_list': latest_patient_list}
    return render(request, 'home/index.html', context)