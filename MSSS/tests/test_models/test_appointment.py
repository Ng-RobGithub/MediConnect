from django.test import TestCase
from .models import Appointment
from datetime import datetime
from .constants import APPOINTMENT_STATUSES
from .models import Patient, Doctor, Location


class AppointmentModelTestCase(TestCase):
    def setUp(self):
        """ Create sample instances for testing """
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
                )
        self.doctor = Doctor.objects.create(
                first_name='Dr.',
                last_name='Smith',
                specialization='Cardiology',
                )
        self.location = Location.objects.create(
                name='Hospital A',
                address='456 Elm St',
                )
        self.appointment = Appointment.objects.create(
                date_and_time=datetime.now(),
                patient=self.patient,
                doctor=self.doctor,
                location=self.location,
                status=APPOINTMENT_STATUSES[0][0],
                reason='Regular checkup',
                duration=60,
                )

    def test_appointment_creation(self):
        """ Test appointment object creation """
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.location, self.location)
        self.assertEqual(self.appointment.status, APPOINTMENT_STATUSES[0][0])
        self.assertEqual(self.appointment.reason, 'Regular checkup')
        self.assertEqual(self.appointment.duration, 60)

    def test_str_representation(self):
        """ Test __str__ method """
        expected_str = f"Appointment for {self.patient} with {self.doctor} on "
        "{self.appointment.date_and_time}"
        self.assertEqual(str(self.appointment), expected_str)
