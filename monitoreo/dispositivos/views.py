from django.shortcuts import render

def inicio(request):
    contexto = {"nombre": "Profe Javier"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "Sensor 2", "valor": 200},
        {"nombre": "Sensor 3", "valor": 300},
    ]

    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
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