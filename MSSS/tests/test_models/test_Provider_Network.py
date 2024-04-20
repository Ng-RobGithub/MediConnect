from django.test import TestCase
from datetime import datetime
from .models import Provider, Specialty, Location, ProviderAvailability
from .models import Appointment, Review, Insurance, TelemedicineAvailability
from .models import License


class ProviderNetworkModelTestCase(TestCase):
    def setUp(self):
        """ Create sample specialty for testing """
        self.specialty = Specialty.objects.create(
                name='Cardiology',
                description='Specialty dealing with heart-related issues',
                )
        """ Create sample provider for testing """
        self.provider = Provider.objects.create(
                name='John Doe Clinic',
                email='john@example.com',
                phone_number='123-456-7890',
                address='123 Main St, Anytown, USA',
                )
        self.provider.specialties.add(self.specialty)
        """ Create sample location for the provider """
        self.location = Location.objects.create(
                provider=self.provider,
                address='123 Main St, Anytown, USA',
                latitude=40.7128,
                longitude=-74.0060,
                )
        """ Create sample provider availability """
        self.provider_availability = ProviderAvailability.objects.create(
                provider=self.provider,
                working_hours='9AM-5PM',
                appointment_slots='15-minute slots',
                )
        """ Create sample appointment """
        self.appointment = Appointment.objects.create(
                provider=self.provider,
                patient='Jane Doe',
                date_and_time=datetime.now(),
                status='Scheduled',
                )
        """ Create sample review """
        self.review = Review.objects.create(
                provider=self.provider,
                patient='Jane Doe',
                rating=4,
                comment='Great experience with Dr. John Doe',
                )
        """ Create sample insurance information """
        self.insurance = Insurance.objects.create(
                provider=self.provider,
                insurance_name='ABC Insurance',
                accepted_plans='Plan A, Plan B',
                )
        """ Create sample telemedicine availability """
        self.telemedicine_availability = (
            TelemedicineAvailability.objects.create(
                provider=self.provider,
                available=True,
                meeting_url='https://example.com/meeting-room',
                )
            )
        """ Create sample license information """
        self.license = License.objects.create(
                provider=self.provider,
                license_number='123456',
                expiration_date='2024-12-31',
                )

    def test_specialty_creation(self):
        """ Test specialty object creation """
        self.assertEqual(self.specialty.name, 'Cardiology')
        self.assertEqual(self.specialty.description, 'Specialty dealing with'
                         ' heart-related issues')

    def test_provider_creation(self):
        """ Test provider object creation """
        self.assertEqual(self.provider.name, 'John Doe Clinic')
        self.assertEqual(self.provider.email, 'john@example.com')

    def test_location_creation(self):
        """ Test location object creation """
        self.assertEqual(self.location.provider, self.provider)

    def test_provider_availability_creation(self):
        """ Test provider availability object creation """
        self.assertEqual(self.provider_availability.provider, self.provider)

    def test_appointment_creation(self):
        """ Test appointment object creation """
        self.assertEqual(self.appointment.provider, self.provider)

    def test_review_creation(self):
        """ Test review object creation """
        self.assertEqual(self.review.provider, self.provider)

    def test_insurance_creation(self):
        """ Test insurance object creation """
        self.assertEqual(self.insurance.provider, self.provider)

    def test_telemedicine_availability_creation(self):
        """ Test telemedicine availability object creation """
        self.assertEqual(self.telemedicine_availability.provider,
                         self.provider)

    def test_license_creation(self):
        """ Test license object creation """
        self.assertEqual(self.license.provider, self.provider)
