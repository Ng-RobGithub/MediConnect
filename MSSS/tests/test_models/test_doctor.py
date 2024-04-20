from django.test import TestCase
from .models.doctor import Doctor
from .forms import DoctorForm


class DoctorModelTestCase(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
                name="John Doe",
                specialization="Cardiology",
                email="john.doe@example.com",
                phone_number="1234567890",
                address="123 Main Street, City, Country"
                )


def test_doctor_creation(self):
    self.assertEqual(self.doctor.name, "John Doe")
    self.assertEqual(self.doctor.specialization, "Cardiology")
    self.assertEqual(self.doctor.email, "john.doe@example.com")
    self.assertEqual(self.doctor.phone_number, "1234567890")
    self.assertEqual(self.doctor.address, "123 Main Street, City, Country")


class DoctorFormTestCase(TestCase):
    def test_valid_form(self):
        form = DoctorForm(data={
            'name': 'John Doe',
            'specialization': 'Cardiology',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'address': '123 Main Street, City, Country'
            })
        self.assertTrue(form.is_valid())


def test_invalid_form(self):
    form = DoctorForm(data={})
    self.assertFalse(form.is_valid())
