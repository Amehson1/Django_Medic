from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.contrib.gis import models

# Create your models here.
STATUS = {('pending', 'Pending'), ('accepted','Accepted'), ('declined','Declined')}

class Location(models.Model):
    pass
    # country
    # state
    # city
    # zip code - longitude, latitude

class Specialization(models.Model):
    name = models.CharField(max_length=200)

class Doctor(models.Model):
    last_name = models.CharField(max_length=200)
    speciality = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    portfolio_number = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return 
    
class Patient(models.Model):
    pass

class RequestConsultation(models.Model):
    """ Patients request consultation with available doctor and the doctor sets an appointment if consultation is accepted"""
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "requests")
    doctor = models.ForeignKey(Doctor,  on_delete=models.CASCADE,related_name= "consultations", verbose_name="Request for consultation")
    symptoms = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self) -> str:
        return f"{self.patient}-{self.status}"

class Appointment(models.Model):
    consult = models.ForeignKey(RequestConsultation, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices={('virtual', 'Virtual'), ('physical','Physical'), ('private','Private')})
    date = models.DateTimeField(verbose_name="Date and Time for appointment")

    def __str__(self) -> str:
        return f"{self.type}-{self.date}"
    
class Symptoms(models.Model):
    name = models.CharField(max_length=200, verbose_name="symptoms")

    def __str__(self) -> str:
        return self.name
    
class Drugs(models.Model):
    name = models.CharField(max_length=200, verbose_name="name of the drug")
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Medical History", related_name="medical_history")
    illness = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptoms)
    drugss = models.ManyToManyField(Drugs)
    allergies = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients_attended", verbose_name="Patients Attended")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.illness} - {self.symptoms} - {self.date}"
    