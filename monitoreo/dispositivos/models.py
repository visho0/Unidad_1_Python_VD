from django.db import models

class Categoria(models.Model):
 nombre = models.CharField(max_length=100)
 descripcion = models.TextField(blank=True, null=True)

 def __str__(self):
   return self.nombre

class Dispositivo(models.Model):
 nombre = models.CharField(max_length=100)
 consumo = models.IntegerField()
 estado = models.BooleanField(default=True)
 

def __str__(self):
   return self.nombre


