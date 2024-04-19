from django.contrib import admin
from .models import patient, appointment, EHR, diagnosis, prescription
from .models import treatment, remote_monitor, Telemed_Integration
from .models import health_monitor, Provider_Network, data_analytic

admin.site.register(patient)
admin.site.register(EHR)
admin.site.register(appointment)
admin.site.register(diagnosis)
admin.site.register(prescription)
admin.site.register(treatment)
admin.site.register(remote_monitor)
admin.site.register(Telemed_Integration)
admin.site.register(health_monitor)
admin.site.register(Provider_Network)
admin.site.register(data_analytic.py)
