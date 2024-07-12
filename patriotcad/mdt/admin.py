from django.contrib import admin
from .models import Officer, Civilian, DriversLicense, Vehicle, Incident, CurrentCall, Report, Citation

admin.site.register(Officer)
admin.site.register(Civilian)
admin.site.register(DriversLicense)
admin.site.register(Vehicle)
admin.site.register(Incident)
admin.site.register(CurrentCall)
admin.site.register(Report)
admin.site.register(Citation)
