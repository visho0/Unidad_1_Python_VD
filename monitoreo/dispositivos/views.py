from django.shortcuts import render
from .models import Dispositivo

def inicio(request):
    #Dispositivos = Dispositivo.objects.all()
    Dispositivos = Dispositivo.objects.select_related("Categoria")

    return render(request, "dispositivos/inicio.html", {
        "dispositivos": Dispositivos
    })

def panel_dispositivo(request):
   dispositivos = [
       {"nombre": "Sensor Temperatura", "consumo": 50},
       {"nombre": "Medidor Solar", "consumo": 120},
       {"nombre": "Sensor Movimiento", "consumo": 30},
       {"nombre": "Calefactor", "consumo": 200},
   ]
   consumo_maximo = 100
   criticos = sum(1 for d in dispositivos if d["consumo"] > consumo_maximo)
   contexto = {
       "dispositivos": dispositivos,
       "consumo_maximo": consumo_maximo,
       "criticos": criticos
   }
   return render(request, "dispositivos/panel.html", contexto)

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    
    return render(request, "dispositivos/inicio.html", {"dispositivo": dispositivo})