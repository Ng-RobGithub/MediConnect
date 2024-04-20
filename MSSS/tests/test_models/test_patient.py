from django.test import TestCase
from .models import Patient


class PatientModelTestCase(TestCase):
    def setUp(self):
        """ Create a sample patient instance for testing """
        self.patient = Patient.objects.create(
                first_name='John',
                last_name='Doe',
                date_of_birth='1990-01-01',
                address='123 Main St',
                phone_number='123-456-7890',
                email='john@example.com',
                emergency_contact_name='Jane Doe',
                emergency_contact_phone_number='987-654-3210',
                relationship_to_patient='Spouse',
                insurance_provider='XYZ Insurance',
                insurance_id='123456789',
                policy_holder='John Doe',
                allergies='Peanuts',
                medications='Med1, Med2',
                past_medical_conditions='None',
                family_medical_history='Heart disease',
                occupation='Developer',
                marital_status='Married',
                preferred_language='English',
                ethnicity='Caucasian',
                religion='None',
                )

        def test_patient_creation(self):
            """ Test patient object creation """
            self.assertEqual(self.patient.first_name, 'John')
            self.assertEqual(self.patient.last_name, 'Doe')
            self.assertEqual(str(self.patient), 'John Doe')

        def test_str_representation(self):
            """ Test __str__ method """
            self.assertEqual(str(self.patient), 'John Doe')

        def test_blank_fields(self):
            """ Test blank fields """
            blank_patient = Patient.objects.create(first_name='Jane',
                                                   last_name='Doe')
            self.assertEqual(blank_patient.allergies, '')

        def test_full_name_property(self):
            """ Test full_name property """
            self.assertEqual(self.patient.full_name, 'John Doe')
