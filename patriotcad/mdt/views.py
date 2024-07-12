from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Officer, Vehicle, Incident, Report
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def officer_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        officer = Officer.objects.create(
            badge_number=data["badge_number"],
            name=data["name"],
            rank=data["rank"],
            department=data["department"],
        )
        return JsonResponse({"id": officer.id}, status=201)
    
    officers = Officer.objects.all()
    data = {"officers": list(officers.values())}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def vehicle_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        vehicle = Vehicle.objects.create(
            license_plate=data["license_plate"],
            make=data["make"],
            model=data["model"],
            year=data["year"],
            color=data["color"],
        )
        return JsonResponse({"id": vehicle.id}, status=201)
    
    vehicles = Vehicle.objects.all()
    data = {"vehicles": list(vehicles.values())}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def incident_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        incident = Incident.objects.create(
            report_number=data["report_number"],
            date_time=data["date_time"],
            location=data["location"],
            description=data["description"],
        )
        return JsonResponse({"id": incident.id}, status=201)
    
    incidents = Incident.objects.all()
    data = {"incidents": list(incidents.values())}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def report_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        incident = get_object_or_404(Incident, id=data["incident_id"])
        officer = get_object_or_404(Officer, id=data["officer_id"])
        report = Report.objects.create(
            incident=incident,
            officer=officer,
            report_text=data["report_text"],
            date_time=data["date_time"],
        )
        return JsonResponse({"id": report.id}, status=201)
    
    reports = Report.objects.all()
    data = {"reports": list(reports.values())}
    return JsonResponse(data)
