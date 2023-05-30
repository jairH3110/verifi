from django.db import models
from django.conf import settings

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
    comentarios =  models.TextField(default='', blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)



class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rango = models.ForeignKey('rangos.Rango', related_name='votes', on_delete=models.CASCADE)