from django.db import models


class TelemedicineAppointment(models.Model):
    appointment_id = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    provider_id = models.ForeignKey('Provider', on_delete=models.CASCADE)
    meeting_url = models.URLField()


class VideoConferencingDetails(models.Model):
    meeting_id = models.CharField(max_length=100)
    host_id = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    meeting_url = models.URLField()


class PatientConsent(models.Model):
    patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE)
    consent_status = models.BooleanField()
    consent_date = models.DateTimeField()
    consent_form = models.FileField(upload_to='consent_forms/')


class ProviderAvailability(models.Model):
    provider_id = models.ForeignKey('Provider', on_delete=models.CASCADE)
    available_time_slots = models.TextField()
    appointment_capacity = models.IntegerField()


class TelehealthEquipment(models.Model):
    equipment_id = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    equipment_model = models.CharField(max_length=100)
    equipment_status = models.CharField(max_length=20)


class CommunicationLog(models.Model):
    communication_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    sender_id = models.CharField(max_length=100)
    recipient_id = models.CharField(max_length=100)
    message_content = models.TextField()


class PaymentTransaction(models.Model):
    payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20)


class TelemedicineIntegration(models.Model):
    encrypted_communication = models.BooleanField()
    authentication_required = models.BooleanField()
    compliance_with_regulations = models.BooleanField()
    error_handling_and_logging = models.BooleanField()


def __str__(self):
    return "Telemedicine Integration Settings"
