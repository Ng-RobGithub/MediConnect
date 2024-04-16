from django.test import TestCase
from .models import Provider, Patient, Treatment, AdverseReaction
from datetime import date


class TreatmentModelTestCase(TestCase):
    def setUp(self):
        """ Create sample provider for testing """
        self.provider = Provider.objects.create(
                name='Dr. Smith',
                contact_number='123-456-7890',
                email='drsmith@example.com',
                specialty='General Medicine',
                credentials='MD',
                )
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='John Doe',
                contact_number='987-654-3210',
                email='johndoe@example.com',
                date_of_birth=date(1985, 5, 15),
                medical_history='Sample medical history',
                )
        """ Create sample treatment for testing """
        self.treatment = Treatment.objects.create(
                name='Sample Treatment',
                description='Sample description',
                start_date=date.today(),
                end_date=None,
                provider=self.provider,
                patient=self.patient,
                treatment_type='Medication',
                dosage='10mg',
                frequency='Once daily',
                instructions='Take with food',
                status='Active',
                )
        """ Create sample adverse reaction for testing """
        self.adverse_reaction = AdverseReaction.objects.create(
                treatment=self.treatment,
                reaction_date=date.today(),
                reaction_details='Sample adverse reaction details',
                )
