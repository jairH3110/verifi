from django.db import models

# Create your models here.

class Rango(models.Model):
    faccion = models.TextField(default='', blank=False)
    raza =  models.TextField(default='', blank=False)
    rango =  models.TextField(default='', blank=False)  
    caracteristicas =  models.TextField(default='', blank=False)
    peligrosidad =  models.TextField(default='', blank=False)
    representantes =  models.TextField(default='', blank=False)
    origen =  models.TextField(default='', blank=False)
    especialidad =  models.TextField(default='', blank=False)
    antiguedad =  models.TextField(default='', blank=False)


