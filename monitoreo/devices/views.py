from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.core.paginator import Paginator
from .models import Measurement
from datetime import datetime, timedelta

def home(request):
    # Using select_related to optimize queries
    devices = Device.objects.select_related("category", "zone", "organization")

    return render(request, "devices/home.html", {
        "devices": devices
    })

def device_panel(request):
   devices = [
       {"name": "Temperature Sensor", "consumption": 50},
       {"name": "Solar Meter", "consumption": 120},
       {"name": "Motion Sensor", "consumption": 30},
       {"name": "Heater", "consumption": 200},
   ]
   max_consumption = 100
   critical = sum(1 for d in devices if d["consumption"] > max_consumption)
   context = {
       "devices": devices,
       "max_consumption": max_consumption,
       "critical": critical
   }
   return render(request, "devices/panel.html", context)

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    return render(request, "devices/detail.html", {"device": device})

def create_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_devices')  # adjust to your urls.py name
    else:
        form = DeviceForm()
    
    return render(request, "devices/create.html", {"form": form})

def measurements_view(request):
    # Aquí puedes agregar la lógica para obtener y filtrar las mediciones
    measurements = []  # Reemplaza esto con la consulta real a tu modelo de mediciones

    return render(request, "devices/measurements.html", {
        "measurements": measurements
    })

