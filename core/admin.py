from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from .models import Destinos, Contacto, Travel ,Excursiones, Excursiontravel
from django.contrib.auth.models import User

# Register your models here.

# admin.site.register(Travel)

class DestinosAdmin(admin.ModelAdmin):
      list_display = ('Id', 'city','country','description','urlImg','tipo') 
      search_fields = ('city', 'country')
      ordering = ('city',)
admin.site.register(Destinos, DestinosAdmin)


class ContactosAdmin(admin.ModelAdmin):
      list_display = ('name', 'lastname','email','subject','message','fecha') 
      search_fields = ('name', 'lastname')
      fields = ('name', 'lastname','email','subject','message','fecha')
      ordering = ('-name',)
admin.site.register(Contacto, ContactosAdmin)

admin.site.site_header = 'fineGap - Turismo'

class ExcursiontravelInline(admin.TabularInline):
    model = Excursiontravel
    extra = 1


class TravelAdmin(admin.ModelAdmin):
    inlines = [ExcursiontravelInline]
    list_display = ('fecha_desde', 'fecha_hasta', 'valor', 'pasajeros', 'destino', 'usuarios')


    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'excursiones':
            kwargs["queryset"] = Excursiones.objects.all().order_by("city")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Travel, TravelAdmin)














# admin.site.site_title = 'Turismo'
# admin.site.index_title = 'Administracion Usuarios'

# videogameStore/admin.py
# class VideogameAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created', 'popular')
#     # ...

#     def popular(self, obj):
#         return "Popular" if obj.rating > 4.5 else "No es popular"

#@admin.register(Travel)
# class TravelAdmin(admin.ModelAdmin):
#     list_display = ('city', 'country')

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field == 'destino':
#             kwargs["queryset"] = Destinos.objects.filter().order_by("tipo")

#         return super().formfield_for_manytomany(db_field, request, **kwargs)
    
# class TraveldestinosInline(admin.TabularInline):
#     model = Travel.destino.through
#     extra = 1

# class UsertravelInline(admin.TabularInline):
#     model = Travel.usuarios.through
#     extra = 1


# admin.site.register(Travel, TravelAdmin)