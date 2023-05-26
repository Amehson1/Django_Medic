from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import DeleteView, UpdateView, FormView

from .models import (
    Doctor,
    RequestConsultation,
    Appointment,
    Symptoms,
    Drugs,
    MedicalHistory,
    Specialization
)
# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse('This is Home Page')
    
   

class CreateDoctor(CreateView):
    model = Doctor
    field = "__all__"
    