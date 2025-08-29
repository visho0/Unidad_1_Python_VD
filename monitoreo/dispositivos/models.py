from django.db import models 

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    # ahora pueden ser nulos hasta que se asignen
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="dispositivos",
        null=True,
        blank=True
    )
    zona = models.ForeignKey(
        Zona,
        on_delete=models.CASCADE,
        related_name="dispositivos",
        null=True,
        blank=True
    )
    consumo_maximo = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)  # en Watts

    def __str__(self):
        # Previene error si aún no tiene categoría
        return f"{self.nombre} ({self.categoria.nombre if self.categoria else 'Sin categoría'})"


class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="mediciones")
    fecha = models.DateTimeField(auto_now_add=True)
    consumo = models.DecimalField(max_digits=8, decimal_places=2)  # Watts medidos

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.consumo} W ({self.fecha.strftime('%Y-%m-%d %H:%M')})"


class Alerta(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="alertas")
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField()
    nivel = models.CharField(
        max_length=20,
        choices=[
            ("INFO", "Info"),
            ("WARNING", "Warning"),
            ("CRITICO", "Crítico"),
        ]
    )

    def __str__(self):
        return f"Alerta {self.nivel} - {self.dispositivo.nombre}"
