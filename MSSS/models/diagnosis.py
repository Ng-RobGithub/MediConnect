from django.db import models
from .provider_network import Provider
from .patient import Patient


class DiagnosisProvider(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialty = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)


class DiagnosisPatient(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    medical_history = models.TextField()


class Diagnosis(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField()
    date_diagnosed = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    category = models.CharField(max_length=50)


class treatmentPlan(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    plan_details = models.TextField()
    medications = models.TextField()
    follow_up_actions = models.TextField()


class diagnosticTest(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    test_results = models.TextField()
