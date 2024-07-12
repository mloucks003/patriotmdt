# Register your models here.
from django.contrib import admin
from .models import Officer, Vehicle, Incident, Report

admin.site.register(Officer)
admin.site.register(Vehicle)
admin.site.register(Incident)
admin.site.register(Report)
