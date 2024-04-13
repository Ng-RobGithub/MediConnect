#!/usr/bin/python

from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
            ]
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone_number = models.CharField(max_length=20)
    relationship_to_patient = models.CharField(max_length=50)
    insurance_provider = models.CharField(max_length=100)
    insurance_id = models.CharField(max_length=50)
    policy_holder = models.CharField(max_length=100)
    allergies = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    past_medical_conditions = models.TextField(blank=True)
    family_medical_history = models.TextField(blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=20, blank=True)
    preferred_language = models.CharField(max_length=50, blank=True)
    ethnicity = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
