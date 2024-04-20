from django.test import TestCase
from .models import Patient, VitalSigns, HealthEvent, HealthMonitoringPlan
from .models import MonitoringAlert
from datetime import datetime


class HealthMonitorModelTestCase(TestCase):
    def setUp(self):
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='John Doe',
                contact_number='123-456-7890',
                email='john@example.com',
                date_of_birth='1990-01-01',
                medical_history='No significant medical history',
                )
        """ Create sample vital signs data for the patient """
        self.vital_signs = VitalSigns.objects.create(
                patient=self.patient,
                timestamp=datetime.now(),
                blood_pressure='120/80 mmHg',
                heart_rate=75,
                respiratory_rate=16,
                temperature=37.0,
                oxygen_saturation=98,
                )
        """ Create sample health event for the patient """
        self.health_event = HealthEvent.objects.create(
                patient=self.patient,
                event_type='Checkup',
                timestamp=datetime.now(),
                details='Routine checkup',
                )
        """ Create sample health monitoring plan for the patient """
        self.health_monitoring_plan = HealthMonitoringPlan.objects.create(
                patient=self.patient,
                plan_name='Daily Monitoring',
                start_date='2024-01-01',
                end_date='2024-01-31',
                active=True,
                )
        """ Create sample monitoring alert for the patient """
        self.monitoring_alert = MonitoringAlert.objects.create(
                patient=self.patient,
                alert_type='Abnormal vital signs',
                timestamp=datetime.now(),
                details='High blood pressure detected',
                )

    def test_patient_creation(self):
        """ Test patient object creation """
        self.assertEqual(self.patient.name, 'John Doe')
        self.assertEqual(self.patient.contact_number, '123-456-7890')
        self.assertEqual(self.patient.email, 'john@example.com')
        self.assertEqual(self.patient.date_of_birth, '1990-01-01')
        self.assertEqual(self.patient.medical_history,
                         'No significant medical history')

    def test_vital_signs_creation(self):
        """ Test vital signs object creation """
        self.assertEqual(self.vital_signs.patient, self.patient)

    def test_health_event_creation(self):
        """ Test health event object creation """
        self.assertEqual(self.health_event.patient, self.patient)

    def test_health_monitoring_plan_creation(self):
        """ Test health monitoring plan object creation """
        self.assertEqual(self.health_monitoring_plan.patient, self.patient)

    def test_monitoring_alert_creation(self):
        """ Test monitoring alert object creation """
        self.assertEqual(self.monitoring_alert.patient, self.patient)
