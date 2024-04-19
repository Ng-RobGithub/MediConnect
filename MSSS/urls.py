from django.urls import path
from . import views

urlpatterns = [
    path('patients/<int:patient_id>/', views.patient_view,
         name='patient_detail'),
    path('appointments/', views.appointment_view, name='appointment_list'),
    path('providers/', views.Provider_Network_view.as_view(),
         name='provider_network'),
    path('telemed/', views.Telemed_Integration_view.as_view(),
         name='telemed_integration'),
    path('ehr/', views.ehr_view, name='ehr'),
    path('prescription/<int:prescription_id>/', views.prescription_view,
         name='prescription_detail'),
    path('monitor/<int:monitor_id>/', views.remote_monitor_view,
         name='remote_monitor_detail'),
    path('treatment/<int:treatment_id>/', views.treatment_view,
         name='treatment_detail'),
    path('data/', views.data_analytic_view, name='data-view'),
    path('api/data/', views.api_data_analytic_view, name='api-data-view'),
]
