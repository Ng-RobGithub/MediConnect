from django.http import JsonResponse
from django.shortcuts import render
from .models import Patient, Appointment, HealthMonitor, ProviderNetwork
from .models import TelemedIntegration, Diagnosis
from .models import Data_Analytic, EHR, Prescription, RemoteMonitor, Treatment
""" from .serializers import ProviderNetworkSerializer, PrescriptionSerializer
"""


def patient(request, patient_id):
    """ Retrieve patient details from the database """
    patient = Patient.objects.get(id=patient_id)
    """Render a template with patient details """
    return render(request, 'patient_detail.html', {'patient': patient})


def appointment(request):
    """ Retrieve list of appointments from the database """
    appointments = Appointment.objects.all()
    """ Serialize appointments data as JSON and return as response """
    data = [{'id': appointment.id, 'date': appointment.date, 'patient':
             appointment.patient_id} for appointment in appointments]
    return JsonResponse(data, safe=False)


def diagnosis(request):
    diagnoses = Diagnosis.objects.all()
    data = [{'id': diag.id, 'name': diag.name} for diag in diagnoses]
    return JsonResponse(data, safe=False)


def health_monitor_list(request):
    health_monitors = HealthMonitor.objects.all()
    data = [{'id': monitor.id, 'name': monitor.name} for monitor in
            health_monitors]
    return JsonResponse(data, safe=False)


class ProviderNetwork(request):
    def get(self, request):
        providers = Provider_Network.objects.all()
        """ Serialize data if needed """
        data = [{'name': provider.name, 'location': provider.location} for
                provider in providers]
        return JsonResponse(data, safe=False)


def telemed_integration_view(request):
    """ Example view function to handle requests related to Telemed
    Integration
    """
    """ Retrieve all Telemed """
    data = TelemedIntegration.objects.all().values()
    return JsonResponse(list(data), safe=False)


def ehr_view(request):
    """ Example view function to handle requests related to EHR """
    ''' Retrieve all EHR data '''
    data = EHR.objects.all().values()
    return JsonResponse(list(data), safe=False)


def prescription_list(request):
    """ Fetch all prescription objects from the database """
    prescriptions = Prescription.objects.all()

    """ Serialize the prescription objects into JSON format """
    data = [{'id': prescription.id, 'name': prescription.name, 'description':
             prescription.description} for prescription in prescriptions]

    """ Return JSON response with prescription data """
    return JsonResponse(data, safe=False)


def remote_monitor_list(request):
    """ Fetch all remote monitor objects from the database """
    remote_monitors = RemoteMonitor.objects.all()

    """ Serialize the remote monitor objects into JSON format """
    data = [{'id': monitor.id, 'name': monitor.name, 'status': monitor.status}
            for monitor in remote_monitors]

    """ Return JSON response with remote monitor data """
    return JsonResponse(data, safe=False)


def treatment_list(request):
    """ Fetch all treatment objects from the database """
    treatments = Treatment.objects.all()

    """ Serialize the treatment objects into JSON format """
    data = [{'id': treatment.id, 'name': treatment.name, 'duration':
             treatment.duration} for treatment in treatments]

    """ Return JSON response with treatment data """
    return JsonResponse(data, safe=False)


def data_analytic(request):
    """ Fetch data from the data_analytic_view model """
    data = data_analytic.objects.all()

    """ Process the data as needed """
    serialized_data = [{'id': item.id, 'field1': item.field1, 'field2':
                        item.field2} for item in data]

    """ Return a JSON response with the serialized data """
    return JsonResponse(serialized_data, safe=False)
