from django.db import models

# Create your models here.
class Torneo(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"

class Equipo(models.Model):
    nombre=models.CharField(max_length=50)
    jugadores=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.jugadores} jugadores"

class Arbitro(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"