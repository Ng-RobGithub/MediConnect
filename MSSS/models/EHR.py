from django.db import models
from .Network_Provider import Provider
from .ElectronicHealthRecord import ElectronicHealthRecord
from .patient import Patient


class EHR(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    encounter_date_time = models.DateTimeField()
    healthcare_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    encounter_type = models.CharField(max_length=100)
    reason_for_encounter = models.TextField()
    primary_diagnosis = models.CharField(max_length=100)
    other_diagnoses = models.TextField(blank=True)
    treatment_provided = models.TextField()
    notes = models.TextField(blank=True)


class VitalSigns(models.Model):
    ehr = models.ForeignKey(ElectronicHealthRecord, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    respiratory_rate = models.IntegerField()
    oxygen_saturation = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                 blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                 blank=True)


class LaboratoryResult(models.Model):
    ehr = models.ForeignKey(ElectronicHealthRecord, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=100)
    result_value = models.CharField(max_length=100)
    reference_range = models.CharField(max_length=100)
    units = models.CharField(max_length=50)
    test_date = models.DateField()


class Procedure(models.Model):
    ehr = models.ForeignKey(ElectronicHealthRecord, on_delete=models.CASCADE)
    procedure_type = models.CharField(max_length=100)
    procedure_date = models.DateField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)


class Medication(models.Model):
    ehr = models.ForeignKey(ElectronicHealthRecord, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    prescribing_provider = models.ForeignKey(Provider,
                                             on_delete=models.CASCADE)


class Allergy(models.Model):
    ehr = models.ForeignKey(ElectronicHealthRecord, on_delete=models.CASCADE)
    allergen = models.CharField(max_length=100)
    reaction = models.TextField()
    severity = models.CharField(max_length=20)


class EHRTimestamps(models.Model):
    ehr = models.OneToOneField(ElectronicHealthRecord,
                               on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"EHR for {self.patient} - {self.date_and_time}"
