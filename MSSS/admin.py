from django.contrib import admin
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
from .models.doctor import Doctor


admin.site.site_header = "mediconnect Admin"
admin.site.site_title = "Medical Service Support System"
admin.site.index_title = "Welcome to mediconnect Admin portal"
admin.site.register(Patient)
admin.site.register(ElectronicHealthRecord)
admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(Prescription)
admin.site.register(Treatment)
admin.site.register(Remote_Monitor)
admin.site.register(Telemed_Integration)
admin.site.register(Health_Monitor)
admin.site.register(Provider)
admin.site.register(Data_Analytic)
admin.site.register(Doctor)
