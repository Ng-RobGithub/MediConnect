from django.http import JsonResponse
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer

def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return JsonResponse(serializer.data, safe=False)

def patient_detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    serializer = PatientSerializer(patient)
    return JsonResponse(serializer.data)

def appointment_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)

def appointment_detail(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    serializer = AppointmentSerializer(appointment)
    return JsonResponse(serializer.data)
