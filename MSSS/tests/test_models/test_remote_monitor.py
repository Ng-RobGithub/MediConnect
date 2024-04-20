from django.test import TestCase
from .models import Patient, RemoteMonitoringDevice, MonitoringData, Alert
from datetime import datetime


class RemoteMonitoringModelTestCase(TestCase):
    def setUp(self):
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='John Doe',
                contact_number='987-654-3210',
                email='johndoe@example.com',
                date_of_birth='1985-05-15',
                medical_history='Sample medical history',
                )
        """ Create sample remote monitoring device for testing """
        self.device = RemoteMonitoringDevice.objects.create(
                device_type='Blood Pressure Monitor',
                serial_number='12345',
                manufacturer='Sample Manufacturer',
                patient=self.patient,
                connection_status='Connected',
                )
        """ Create sample monitoring data for testing """
        self.monitoring_data = MonitoringData.objects.create(
                device=self.device,
                timestamp=datetime.now(),
                vital_signs={'blood_pressure': '120/80', 'heart_rate': 70},
                )
        """ Create sample alert for testing """
        self.alert = Alert.objects.create(
                patient=self.patient,
                timestamp=datetime.now(),
                alert_message='Abnormal vital signs detected',
                )
