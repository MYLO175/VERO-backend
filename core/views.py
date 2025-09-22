from django.shortcuts import render

from django.http import HttpResponse

def ping(request):
    return HttpResponse("pong 🏓")



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WaitlistEntry

@csrf_exempt
def waitlist_create(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    data = json.loads(request.body or "{}")
    email = (data.get("email") or "").strip()
    if not email:
        return JsonResponse({"error": "email required"}, status=400)
    entry = WaitlistEntry.objects.create(
        email=email,
        name=(data.get("name") or "").strip(),
        company=(data.get("company") or "").strip(),
        note=(data.get("note") or "").strip(),
    )
    return JsonResponse({"ok": True, "id": entry.id})