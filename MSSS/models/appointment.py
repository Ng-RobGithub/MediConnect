#!/usr/bin/python

from django.db import models
from .constants import APPOINTMENT_STATUSES


class Appointment(models.Model):
    date_and_time = models.DateTimeField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUSES)
    reason = models.TextField(blank=True)
    duration = models.PositiveIntegerField(default=60)  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"Appointment for {self.patient} with {self.doctor} on"
    "{self.date_and_time}"
