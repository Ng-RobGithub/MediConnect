from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DoctorForm
from .models.doctor import Doctor
from .models.patient import Patient
from .models.ehr import ElectronicHealthRecord
from .models.appointment import Appointment
from .models.diagnosis import Diagnosis
from .models.prescription import Prescription
from .models.treatment import Treatment
from .models.remote_monitor import Remote_Monitor
from .models.telemed_integration import Telemed_Integration
from .models.health_monitor import Health_Monitor
from .models.provider_network import Provider
from .models.data_analytic import Data_Analytic
from .models.data_analytic import AnalyticalResult


def index(request):
    return HttpResponse("Hello, world. You're at the MSSS index.")


def patient_view(request, patient_id):
    try:
        """ Retrieve patient details from the database """
        patients = Patient.objects.get(id=patient_id)
        """ Serialize patient data as JSON and return as response """
        data = [{'id': patient.id, 'name': patient.name, 'age': patient.age}
                for patient in patients]
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)


def doctor_view(request):
    """ Retrieve all doctors from the database """
    doctors = Doctor.objects.all()

    """ Pass the doctors data to the template for rendering """
    return render(request, 'doctor_list.html', {'doctors': doctors})


def doctor_form(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
            """
            Replace 'success_url' with the
            URL you want to redirect to after successful form submission
            """
        else:
            form = DoctorForm()
            return render(request, 'doctor_form.html', {'form': form})


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


def provider_network_view(request):
    provider_network = Provider.objects.all()
    """ Serialize data if needed """
    data = [{'name': provider.name, 'location':
             provider.location} for provider in
            provider_network]
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
    data = ElectronicHealthRecord.objects.all().values()
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


def api_data_analytic_view(request):
    """ Retrieve analytical results from the database or other sources """
    analytical_results = AnalyticalResult.objects.all()

    """ Serialize the analytical results into JSON format """
    data = [{'task_id': result.task_id, 'result_data': result.result_data}
            for result in analytical_results]

    """ Return the serialized data as a JSON response """
    return JsonResponse(data, safe=False)
