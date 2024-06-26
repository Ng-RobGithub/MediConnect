from django.db import models
from .patient import Patient


class Health_Monitor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    monitoring_date = models.DateField()
    monitoring_result = models.TextField()


class HealthMonitoredPatient(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    medical_history = models.TextField()


class VitalSigns(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    oxygen_saturation = models.IntegerField()


class HealthEvent(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    details = models.TextField()


class health_monitoringPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)


class MonitoringAlert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    details = models.TextField()


def __str__(self):
    return f"Health Monitor for {self.patient}"
