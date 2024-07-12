from django.db import models

class Officer(models.Model):
    STATUS_CHOICES = [
        ('10-8', 'On Duty'),
        ('10-7', 'Off Duty'),
    ]

    badge_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='Unknown')
    rank = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='10-8')
    attached_calls = models.ManyToManyField('CurrentCall', blank=True)

    def __str__(self):
        return f'{self.rank} {self.first_name} {self.last_name} ({self.badge_number})'

class Civilian(models.Model):
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100, default='Unknown')
    drivers_license_number = models.CharField(max_length=20, unique=True)
    registered_vehicles = models.ManyToManyField('Vehicle', blank=True)
    address = models.CharField(max_length=200, default='Unknown')
    warrants = models.TextField(blank=True, default='')
    citations = models.ManyToManyField('Citation', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.drivers_license_number})'

class DriversLicense(models.Model):
    number = models.CharField(max_length=20, unique=True)
    attached_civilian = models.OneToOneField(Civilian, on_delete=models.CASCADE)

    def __str__(self):
        return f'Drivers License {self.number}'

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=50, default='Unknown')
    model = models.CharField(max_length=50, default='Unknown')
    year = models.IntegerField(default=2000)
    color = models.CharField(max_length=20, default='Unknown')
    registered_civilian = models.ForeignKey(Civilian, null=True, on_delete=models.SET_NULL)
    valid = models.BooleanField(default=True)
    bolos = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.license_plate} - {self.make} {self.model}'

class Incident(models.Model):
    report_number = models.CharField(max_length=20, unique=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200, default='Unknown')
    description = models.TextField()

    def __str__(self):
        return f'Incident {self.report_number}'

class CurrentCall(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Low')
    officers_attached = models.ManyToManyField(Officer, blank=True)
    location = models.CharField(max_length=200, default='Unknown')
    description = models.TextField(default='No description')

    def __str__(self):
        return f'Call at {self.location} with priority {self.priority}'

class Report(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    report_text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.officer} on {self.date_time}'

class Citation(models.Model):
    attached_civilian = models.ForeignKey(Civilian, on_delete=models.CASCADE)
    reason = models.TextField()
    date = models.DateTimeField()
    judgment = models.TextField()

    def __str__(self):
        return f'Citation for {self.attached_civilian} on {self.date}'
