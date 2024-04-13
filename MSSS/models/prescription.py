#!/usr/bin/python

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()


class Prescriber(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)


class Prescription(models.Model):
    prescription_id = models.CharField(max_length=100)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    quantity = models.IntegerField()
    instructions = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescriber = models.ForeignKey(Prescriber, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    date_issued = models.DateField()


class PrescriptionHistory(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    date_filled = models.DateField()
    filled_quantity = models.IntegerField()


class MedicationInteraction(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=100)
    interaction_description = models.TextField()
