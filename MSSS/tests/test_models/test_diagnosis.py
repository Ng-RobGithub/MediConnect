from django.test import TestCase
from .models import Diagnosis, Provider, Patient


class DiagnosisModelTestCase(TestCase):
    def setUp(self):
        """ Create sample instances for testing """
        self.provider = Provider.objects.create(
                name='Dr. Smith',
                contact_number='123-456-7890',
                email='smith@example.com',
                specialty='Cardiology',
                credentials='MD'
                )
        self.patient = Patient.objects.create(
                name='John Doe',
                contact_number='987-654-3210',
                email='john@example.com',
                date_of_birth='1990-01-01',
                medical_history='Some medical history'
                )
        self.diagnosis = Diagnosis.objects.create(
                code='D001',
                description='Description of diagnosis',
                date_diagnosed='2024-01-01',
                provider=self.provider,
                patient=self.patient,
                status='Pending',
                category='Category'
                )

    def test_diagnosis_creation(self):
        """ Test diagnosis object creation """
        self.assertEqual(self.diagnosis.code, 'D001')
        self.assertEqual(self.diagnosis.status, 'Pending')
