from django.contrib import admin
from .models import Destinos, Usuario, Contacto

# Register your models here.

# admin.site.register(Destinos)
# admin.site.register(Usuario)
# admin.site.register(Contacto)

class DestinosAdmin(admin.ModelAdmin):
      list_display = ('Id', 'city','country','description','urlImg','tipo') #Ahora la interfaz mostrará nombre y email de cada usuario.
      search_fields = ('city', 'country')
      # fields = ('name', 'lastname','email','subject','message','fecha')
      ordering = ('city',)
admin.site.register(Destinos, DestinosAdmin)

class UsuariosAdmin(admin.ModelAdmin):
      list_display = ('name', 'email') #Ahora la interfaz mostrará nombre y email de cada usuario.
      search_fields = ('name', 'email')
    #   date_hierarchy = 'created'
admin.site.register(Usuario, UsuariosAdmin)

class ContactosAdmin(admin.ModelAdmin):
      list_display = ('name', 'lastname','email','subject','message','fecha') #Ahora la interfaz mostrará nombre y email de cada usuario.
      search_fields = ('name', 'lastname')
      fields = ('name', 'lastname','email','subject','message','fecha')
      ordering = ('-name',)
admin.site.register(Contacto, ContactosAdmin)

admin.site.site_header = 'fineGap - Turismo'












# admin.site.site_title = 'Turismo'
# admin.site.index_title = 'Administracion Usuarios'

# videogameStore/admin.py
# class VideogameAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created', 'popular')
#     # ...

#     def popular(self, obj):
#         return "Popular" if obj.rating > 4.5 else "No es popular"

