from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from .models import Destinos, Contacto, Travel, Traveldestinos, Usertravel
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

class TraveldestinosInline(admin.TabularInline):
    model = Traveldestinos
    extra = 1

class UsertravelInline(admin.TabularInline):
    model = Usertravel
    extra = 1


class TravelAdmin(admin.ModelAdmin):
    inlines = [UsertravelInline,TraveldestinosInline]
    # inlines = [TraveldestinosInline]
    list_display = ('fecha_desde', 'fecha_hasta', 'valor', 'pasajeros')


    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'destino':
            kwargs["queryset"] = Destinos.objects.all().order_by("tipo")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'usuarios':
            kwargs["queryset"] = User.objects.all().order_by("username")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Travel, TravelAdmin)

class TraveldestinosAdmin(admin.ModelAdmin):
      list_display = ('travel', 'destino','fecha') 
      search_fields = ('fecha', 'destino')
      fields = ('travel', 'destino','fecha')
      ordering = ('fecha',)
admin.site.register(Traveldestinos,TraveldestinosAdmin)

class UsertravelAdmin(admin.ModelAdmin):
      list_display = ('travel', 'fecha') 
      search_fields = ('fecha', 'usuario')
      fields = ('travel', 'usuario','fecha')
      ordering = ('fecha',)
admin.site.register(Usertravel,UsertravelAdmin)


# class TravelAdmin(admin.ModelAdmin):
#       list_display = ('destino', 'fecha_desde','fecha_hasta','valor','pasajeros') #Ahora la interfaz mostrará esto.
#       search_fields = ('destino', 'fecha_desde')
#       fields = ('destino', 'fecha_desde','fecha_hasta','valor','pasajeros')
#       ordering = ('fecha_desde',)
# admin.site.register(Travel, TravelAdmin)










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