from django.test import TestCase
from MSSS.models import Patient, Provider
from .models import TelemedicineAppointment, VideoConferencingDetails
from .models import PatientConsent, ProviderAvailability, TelehealthEquipment
from .models import CommunicationLog, PaymentTransaction
from .models import TelemedicineIntegration
from datetime import datetime


class TelemedIntegrationModelTestCase(TestCase):
    def setUp(self):
        """ Create sample patient for testing """
        self.patient = Patient.objects.create(
                name='Jane Doe',
                contact_number='123-456-7890',
                email='jane@example.com',
                date_of_birth='1990-01-01',
                medical_history='Sample medical history',
                )
        """ Create sample provider for testing """
        self.provider = Provider.objects.create(
                name='John Doe Clinic',
                email='john@example.com',
                phone_number='123-456-7890',
                address='123 Main St, Anytown, USA',
                )
        """ Create sample telemedicine appointment """
        self.telemedicine_appointment = TelemedicineAppointment.objects.create(
                appointment_id='123456',
                date_and_time=datetime.now(),
                patient_id=self.patient,
                provider_id=self.provider,
                meeting_url='https://example.com/meeting-room',
                )
        """ Create sample video conferencing details """
        self.video_conferencing_details = (
            VideoConferencingDetails.objects.create(
                meeting_id='abcdef',
                host_id='host123',
                access_token='token123',
                meeting_url='https://example.com/meeting-room',
                )
                )
        """ Create sample patient consent """
        self.patient_consent = PatientConsent.objects.create(
                patient_id=self.patient,
                consent_status=True,
                consent_date=datetime.now(),
                consent_form='consent_form.pdf',
                )
        """ Create sample provider availability """
        self.provider_availability = ProviderAvailability.objects.create(
                provider_id=self.provider,
                available_time_slots='9AM-5PM',
                appointment_capacity=10,
                )
        """ Create sample telehealth equipment """
        self.telehealth_equipment = TelehealthEquipment.objects.create(
                equipment_id='equip123',
                equipment_type='Camera',
                equipment_model='Model A',
                equipment_status='Available',
                )
        """ Create sample communication log """
        self.communication_log = CommunicationLog.objects.create(
                communication_type='Email',
                timestamp=datetime.now(),
                sender_id='sender123',
                recipient_id='recipient456',
                message_content='Sample message content',
                )
        """ Create sample payment transaction """
        self.payment_transaction = PaymentTransaction.objects.create(
                payment_id='payment123',
                amount=100.00,
                payment_date=datetime.now(),
                payment_status='Success',
                )
        """ Create sample telemedicine integration settings """
        self.telemedicine_integration = TelemedicineIntegration.objects.create(
                encrypted_communication=True,
                authentication_required=True,
                compliance_with_regulations=True,
                error_handling_and_logging=True,
                )
