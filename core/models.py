from django.db import models
from django.core.exceptions import ValidationError
from .choices import tipos

# Create your models here.

class Usuario(models.Model):
    # Campos
    name = models.CharField(
        max_length=20,
        verbose_name='nombre',
        )
    email = models.EmailField(
        max_length=100,
        primary_key=True,
        verbose_name='email',
        )
    password = models.CharField(
        max_length=100,
        verbose_name='contraseña',
        )

    # Metadata
    class Meta:
        ordering = ["name"]

    # Metodos
    def detalle_usuario(self):
        return f"{self.name}"
    
    def __str__(self):
        return self.detalle_usuario()

#------------------------------------------------------------------

class Travel(models.Model):
    # Campos
    destino = models.CharField(
        max_length=100,
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
        verbose_name='contraseña',
        )
    usuarios = models.ManyToManyField(
        Usuario, 
        through="usertravel",
        verbose_name='usuarios',
        )
    
    # Metadata
    class Meta:
        ordering = ["destino"]

    # Metodos
    def travel_usuario(self):
        return f"{self.usuarios} -- {self.destino}"
    
    def __str__(self):
        return self.travel_usuario()

#------------------------------------------------------------------

class Usertravel(models.Model):
    # Campos
    travel = models.ForeignKey(
        Travel,
        on_delete=models.CASCADE,
    )
    usuarios = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
    )

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
    email = models.ForeignKey(
        Usuario,
        null=False,
        blank=False,
        related_name='usuarios',
        on_delete=models.CASCADE,
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
