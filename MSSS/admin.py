from django.contrib import admin
from .models import Patient.py, Appointment.py, EHR.py, diagnosis.py, prescription.py
from .models import presription.py, medication.py, remote_monitor.py, telemed.py
from .model import health_monitor.py, provider_network.py, data_analytic.py

admin.site.register(Patient.py)
admin.site.register(EHR.py)
admin.site.register(Appointment.py)
admin.site.register(diagnosis.py)
admin.site.register(prescription.py)
admin.site.register(medication.py)
admin.site.register(remote_monitor.py)
admin.site.register(telemed.py)
admin.site.register(health_monitor.py)
admin.site.register(provider_network.py)
admin.site.register(data_analytic.py)
