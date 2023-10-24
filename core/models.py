from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Viaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destino = models.CharField(max_length=100)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(null=True)
    valor = models.FloatField(default=0)
    pasajeros = models.IntegerField(default=1)

class FormContacto(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

class Destinos(models.Model):
    Id = models.CharField(max_length=20, verbose_name='ID de Destino')
    city = models.CharField(max_length=20, verbose_name='Ciudad')
    country = models.CharField(max_length=100, verbose_name='Pais')
    description = models.CharField(max_length=1000, verbose_name='Descripcion')
    urlImg = models.ImageField(upload_to='locations-img', null=True, verbose_name='Destinos')
    activo = models.BooleanField(verbose_name='Estado (activo/inactivo)')
    tipo = models.BooleanField(verbose_name='Tipo (elegidos/recomendados)')

    def clean_Id(self):
        return self.cleaned_data['Id']
    
    def clean_city(self):
        return self.cleaned_data['city']
    
    def clean_country(self):
        return self.cleaned_data['country']
