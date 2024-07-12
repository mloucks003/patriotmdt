from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Officer, Vehicle, Incident, Report, Civilian, CurrentCall, Citation, DriversLicense
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def officer_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        officer = Officer.objects.create(
            badge_number=data["badge_number"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            rank=data["rank"],
            department=data["department"],
            status=data["status"],
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
        civilian = get_object_or_404(Civilian, id=data["registered_civilian_id"])
        vehicle = Vehicle.objects.create(
            license_plate=data["license_plate"],
            make=data["make"],
            model=data["model"],
            year=data["year"],
            color=data["color"],
            registered_civilian=civilian,
            valid=data["valid"],
            bolos=data.get("bolos", "")
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

@csrf_exempt
@require_http_methods(["GET", "POST"])
def civilian_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        civilian = Civilian.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            drivers_license_number=data["drivers_license_number"],
            address=data["address"],
            warrants=data.get("warrants", "")
        )
        return JsonResponse({"id": civilian.id}, status=201)
    
    civilians = Civilian.objects.all()
    data = {"civilians": list(civilians.values())}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def current_call_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        current_call = CurrentCall.objects.create(
            priority=data["priority"],
            location=data["location"],
            description=data["description"],
        )
        if "officers_attached" in data:
            officers = Officer.objects.filter(id__in=data["officers_attached"])
            current_call.officers_attached.set(officers)
        return JsonResponse({"id": current_call.id}, status=201)
    
    current_calls = CurrentCall.objects.all()
    data = {"current_calls": list(current_calls.values())}
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def citation_list(request):
    if request.method == "POST":
        data = json.loads(request.body)
        civilian = get_object_or_404(Civilian, id=data["attached_civilian_id"])
        citation = Citation.objects.create(
            attached_civilian=civilian,
            reason=data["reason"],
            date=data["date"],
            judgment=data["judgment"],
        )
        return JsonResponse({"id": citation.id}, status=201)
    
    citations = Citation.objects.all()
    data = {"citations": list(citations.values())}
    return JsonResponse(data)
