from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    specialties = models.ManyToManyField('Specialty')


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Location(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class ProviderAvailability(models.Model):
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE)
    working_hours = models.CharField(max_length=100)
    appointment_slots = models.TextField()


class Appointment(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=20)


class Review(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


class Insurance(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    insurance_name = models.CharField(max_length=100)
    accepted_plans = models.TextField()


class TelemedicineAvailability(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    available = models.BooleanField()
    meeting_url = models.URLField()


class License(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
    expiration_date = models.DateField()
