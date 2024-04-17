"""
URL configuration for mediconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mediconnect/', include('mediconnect.urls')),
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
