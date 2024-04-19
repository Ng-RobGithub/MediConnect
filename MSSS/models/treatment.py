from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialty = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    medical_history = models.TextField()


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    instructions = models.TextField()
    status = models.CharField(max_length=50)


class AdverseReaction(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    reaction_date = models.DateField()
    reaction_details = models.TextField()
