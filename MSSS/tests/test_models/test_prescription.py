from django.test import TestCase
from .models import Patient, Prescriber, Pharmacy, Prescription
from .models import PrescriptionHistory, MedicationInteraction
from datetime import date


class PrescriptionModelTestCase(TestCase):
    def setUp(self):
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='John Doe',
                age=30,
                gender='Male',
                medical_history='Sample medical history',
                )
        """ Create sample prescriber for testing """
        self.prescriber = Prescriber.objects.create(
                name='Dr. Smith',
                contact_number='123-456-7890',
                email='drsmith@example.com',
                specialty='General Medicine',
                license_number='123456',
                )
        """ Create sample pharmacy for testing """
        self.pharmacy = Pharmacy.objects.create(
                name='ABC Pharmacy',
                location='123 Main St, Anytown, USA',
                contact_number='123-456-7890',
                )
        """ Create sample prescription for testing """
        self.prescription = Prescription.objects.create(
                prescription_id='123456',
                medication_name='Aspirin',
                dosage='10mg',
                frequency='Twice daily',
                quantity=30,
                instructions='Take with food',
                patient=self.patient,
                prescriber=self.prescriber,
                pharmacy=self.pharmacy,
                status='Active',
                date_issued=date.today(),
                )
        """ Create sample prescription history for testing """
        self.prescription_history = PrescriptionHistory.objects.create(
                prescription=self.prescription,
                date_filled=date.today(),
                filled_quantity=30,
                )
        """ Create sample medication interaction for testing """
        self.medication_interaction = MedicationInteraction.objects.create(
                prescription=self.prescription,
                interaction_type='Drug Interaction',
                interaction_description='Description of drug interaction',
                )
