from django.db import models

# Create your models here.
from django.db import models

class Officer(models.Model):
    badge_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.rank} {self.name} ({self.badge_number})'

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.license_plate} - {self.make} {self.model}'

class Incident(models.Model):
    report_number = models.CharField(max_length=20, unique=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'Incident {self.report_number}'

class Report(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    report_text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.officer} on {self.date_time}'

