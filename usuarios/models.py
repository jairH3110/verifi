from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.TextField(default='', blank=False)
    modelo =  models.TextField(default='', blank=False)
    prompt =  models.TextField(default='', blank=False)  
    resultado =  models.URLField(default='', blank=False)
    fecha =  models.TextField(default='', blank=False)
