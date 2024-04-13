#!/usr/bin/python

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    medical_history = models.TextField()


class RemoteMonitoringDevice(models.Model):
    device_type = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    connection_status = models.CharField(max_length=50)


class MonitoringData(models.Model):
    device = models.ForeignKey(RemoteMonitoringDevice,
                               on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    vital_signs = models.JSONField()
    """Store vital signs data as JSON """


class Alert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    alert_message = models.TextField()
