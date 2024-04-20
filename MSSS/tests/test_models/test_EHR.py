from django.test import TestCase
from .models import Patient, Provider, ElectronicHealthRecord, VitalSigns
from .models import LaboratoryResult, Procedure, Medication, Allergy
from datetime import datetime


class EHRModelTestCase(TestCase):
    def setUp(self):
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='John Doe',
                contact_number='987-654-3210',
                email='johndoe@example.com',
                date_of_birth='1985-05-15',
                medical_history='Sample medical history',
                )
        """ Create sample provider for testing """
        self.provider = Provider.objects.create(
                name='Dr. Smith',
                contact_number='123-456-7890',
                email='drsmith@example.com',
                specialty='Cardiology',
                credentials='MD',
                )
        """ Create sample electronic health record for testing """
        self.ehr = ElectronicHealthRecord.objects.create(
                patient=self.patient,
                encounter_date_time='2024-04-12 10:00:00',
                healthcare_provider=self.provider,
                encounter_type='Checkup',
                reason_for_encounter='Routine checkup',
                primary_diagnosis='Hypertension',
                treatment_provided='Prescribed medication',
                )

    def test_vital_signs_creation(self):
        """ Test creating vital signs for the EHR """
        vital_signs = VitalSigns.objects.create(
                ehr=self.ehr,
                blood_pressure='120/80',
                heart_rate=70,
                temperature=98.6,
                respiratory_rate=16,
                oxygen_saturation=98,
                )
        self.assertIsNotNone(vital_signs)

    def test_laboratory_result_creation(self):
        """ Test creating laboratory result for the EHR """
        laboratory_result = LaboratoryResult.objects.create(
                ehr=self.ehr,
                test_type='Blood Test',
                result_value='Normal',
                reference_range='0-100',
                units='mg/dL',
                test_date='2024-04-12',
                )
        self.assertIsNotNone(laboratory_result)

    def test_procedure_creation(self):
        """ Create sample procedure for testing """
        self.procedure = Procedure.objects.create(
                ehr=self.ehr,
                procedure_type='Sample Procedure Type',
                procedure_date=datetime.now(),
                provider=self.provider,
                notes='Sample Procedure Notes',
                )

    def test_medication_creation(self):
        """ Create sample medication for testing """
        self.medication = Medication.objects.create(
                ehr=self.ehr,
                medication_name='Sample Medication',
                dosage='10 mg',
                frequency='Once daily',
                start_date=datetime.now(),
                prescribing_provider=self.provider,
                )

    def test_allergy_creation(self):
        """ Create sample allergy for testing """
        self.allergy = Allergy.objects.create(
                ehr=self.ehr,
                allergen='Peanuts',
                reaction='Rash',
                severity='Mild',
                )
