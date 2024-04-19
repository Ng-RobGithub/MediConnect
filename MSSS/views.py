from django.http import JsonResponse
from .models import Patient, Appointment, Health_Monitor, Provider_Network
from .models import Telemed_Integration, Diagnosis
from .models import Data_Analytic, EHR, Prescription, Remote_Monitor, Treatment


def patient_view(request, patient_id):
    """ Retrieve patient details from the database """
    patients = Patient.objects.all()
    """ Serialize patient data as JSON and return as response """
    data = [{'id': patient.id, 'name': patient.name, 'age': patient.age} for
            patient in patients]
    return JsonResponse(data, safe=False)


def appointment_view(request):
    """ Retrieve list of appointments from the database """
    appointments = Appointment.objects.all()
    """ Serialize appointments data as JSON and return as response """
    data = [{'id': appointment.id, 'date': appointment.date, 'patient':
             appointment.patient_id} for appointment in appointments]
    return JsonResponse(data, safe=False)


def diagnosis_view(request):
    diagnoses = Diagnosis.objects.all()
    data = [{'id': diag.id, 'name': diag.name} for diag in diagnoses]
    return JsonResponse(data, safe=False)


def health_monitor_view(request):
    health_monitors = Health_Monitor.objects.all()
    data = [{'id': monitor.id, 'name': monitor.name} for monitor in
            health_monitors]
    return JsonResponse(data, safe=False)


def Provider_Network_view(request):
    provider_networks = Provider_Network.objects.all()
    """ Serialize data if needed """
    data = [{'name': provider_network.name, 'location':
             provider_network.location} for provider_network in
            provider_networks]
    return JsonResponse(data, safe=False)


def telemed_integration_view(request):
    """ Example view function to handle requests related to Telemed
    Integration
    """
    """ Retrieve all Telemed """
    data = Telemed_Integration.objects.all().values()
    return JsonResponse(list(data), safe=False)


def ehr_view(request):
    """ Example view function to handle requests related to EHR """
    ''' Retrieve all EHR data '''
    data = EHR.objects.all().values()
    return JsonResponse(list(data), safe=False)


def prescription_view(request):
    """ Fetch all prescription objects from the database """
    prescriptions = Prescription.objects.all()

    """ Serialize the prescription objects into JSON format """
    data = [{'id': prescription.id, 'name': prescription.name, 'description':
             prescription.description} for prescription in prescriptions]

    """ Return JSON response with prescription data """
    return JsonResponse(data, safe=False)


def remote_monitor_view(request):
    """ Fetch all remote monitor objects from the database """
    remote_monitors = Remote_Monitor.objects.all()

    """ Serialize the remote monitor objects into JSON format """
    data = [{'id': monitor.id, 'name': monitor.name, 'status': monitor.status}
            for monitor in remote_monitors]

    """ Return JSON response with remote monitor data """
    return JsonResponse(data, safe=False)


def treatment_view(request):
    """ Fetch all treatment objects from the database """
    treatments = Treatment.objects.all()

    """ Serialize the treatment objects into JSON format """
    data = [{'id': treatment.id, 'name': treatment.name, 'duration':
             treatment.duration} for treatment in treatments]

    """ Return JSON response with treatment data """
    return JsonResponse(data, safe=False)


def data_analytic_view(request):
    """ Fetch data from the data_analytic model """
    data_analytics = Data_Analytic.objects.all()
    """ Process the data as needed """
    serialized_data = [{'id': data_analytic.id, 'field1': data_analytic.field1,
                        'field2': data_analytic.field2} for data_analytic in
                       data_analytics]
    """ Return a JSON response with the serialized data """
    return JsonResponse(serialized_data, safe=False)
