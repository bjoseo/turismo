from django.db import models
from django.core.exceptions import ValidationError
from .choices import tipos
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

#------------------------------------------------------------------
# tabla que contiene los destinos que se pueden contratar
#------------------------------------------------------------------

class Destinos(models.Model):
    # Campos
    Id = models.CharField(max_length=20, verbose_name='ID de Destino')
    city = models.CharField(
        max_length=20,
        verbose_name='Ciudad',
        )
    country = models.CharField(
        max_length=100, 
        verbose_name='Pais',
        )
    description = models.CharField(
        max_length=1000, 
        verbose_name='Descripcion',
        )
    urlImg = models.ImageField(
        upload_to='locations-img', 
        null=True, 
        verbose_name='Destinos',
        )
    tipo = models.CharField(
        max_length=1, 
        default=1,
        choices=tipos,
        verbose_name='Estado',
        )

    # Metadata
    class Meta:
        ordering = ["city"]

    # Metodos
    def detalle_destinos(self):
        return f"{self.city} -- {self.country}"
    
    def __str__(self):
        return self.detalle_destinos()


    def clean_Id(self):
        return self.cleaned_data['Id']
    
    def clean_city(self):
        return self.cleaned_data['city']
    
    def clean_country(self):
        return self.cleaned_data['country']


#------------------------------------------------------------------
# tabla que contiene las excursiones que se pueden contratar
#------------------------------------------------------------------

class Excursiones(models.Model):
    # Campos
    city = models.CharField(
        max_length=20,
        verbose_name='Ciudad',
        )
    description = models.CharField(
        max_length=1000, 
        verbose_name='Descripcion',
        )
    valor = models.FloatField(
        default=0,
        verbose_name='valor',
        )
    tipo = models.CharField(
        max_length=1, 
        default=1,
        # choices=estado,
        verbose_name='Estado',
        )

    # Metadata
    class Meta:
        ordering = ["city"]

    # Metodos
    def detalle_excursiones(self):
        return f"{self.city} -- {self.description}"
    
    def __str__(self):
        return self.detalle_excursiones()
  
    def clean_city(self):
        return self.cleaned_data['city']
    

#------------------------------------------------------------------
# Tabla Travel para registrar cada viaje contratado por un usuario
#------------------------------------------------------------------

class Travel(models.Model):
    # Campos
    destino = models.ForeignKey(
        Destinos, 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        verbose_name='Destino',
        )
    fecha_desde = models.DateField(
        null=True,
        verbose_name='Fecha Desde',
        )
    fecha_hasta = models.DateField(
        null=True,
        verbose_name='Fecha hasta',
        )
    valor = models.FloatField(
        default=0,
        verbose_name='valor',
        )
    pasajeros = models.SmallIntegerField(
        default=1,
        verbose_name='pasajeros',
        )
    usuarios = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        verbose_name='Usuario',
        )
    excursiones = models.ManyToManyField(
        Excursiones, 
        through="Excursiontravel",
        blank=True, 
        verbose_name='Excursion',
        )


    # Metodos
    def travel_destinos(self):
        return f"{self.excursiones} -- {self.destino}"
    
    def __str__(self):
        return self.travel_destinos()
    
#------------------------------------------------------------------
# Tabla intermedia para trabajar con relaciones many to many (Travel - Usuarios)
#------------------------------------------------------------------

class Excursiontravel(models.Model):
    # Campos
    travel = models.ForeignKey(
        Travel,
        on_delete=models.CASCADE,
         null=True,
         blank=True, 
        verbose_name="Travel",
    )
    excursiones = models.ForeignKey(
        Excursiones,
        on_delete=models.CASCADE,
         null=True,
         blank=True, 
        verbose_name="Excursiones",
    )

        # Metodos
    def travel_excursiones(self):
        return f"{self.travel} -- {self.excursiones}"
    
    def __str__(self):
        return self.travel_excursiones()
    
#------------------------------------------------------------------
# Tabla para registrar mensajes de usuarios
#------------------------------------------------------------------

class Contacto(models.Model):
    # Campos
    name = models.CharField(
        max_length=20,
        verbose_name='nombre',
        )
    lastname = models.CharField(
        max_length=20,
        verbose_name='Apellido',
        )
    email = models.CharField(
        max_length=200,
        verbose_name='Email',
        )
    subject = models.CharField(
        max_length=200,
        verbose_name='Asunto',
        )
    message = models.CharField(
        max_length=500,
         verbose_name='Mensaje',
        )
    fecha = models.DateField(
        null=True,
        verbose_name='Fecha',
        )
    
    # Metadata
    class Meta:
        ordering = ["fecha"]

    # Metodos
    def detalle_FormContacto(self):
        return f"{self.name}"
    
    def __str__(self):
        return self.detalle_FormContacto()


#------------------------------------------------------------------
# Tabla intermedia para trabajar con relaciones many to many (Travel - Usuarios)
#------------------------------------------------------------------

# class Usertravel(models.Model):
#     # Campos
#     travel = models.ForeignKey(
#         Travel,
#         on_delete=models.CASCADE,
#          null=True,
#          blank=True, 
#         verbose_name="Travel",
#     )
#     usuarios = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#          null=True,
#          blank=True, 
#         verbose_name="Usuario",
#     )
#     fecha = models.DateField(
#         null=True,
#         verbose_name='Fecha',
#         )


    

