# finegap/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('CreateUsuario/', views.Create_Usuario, name='CreateUsuario'),
    path('contacto/', views.contacto, name='contacto'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('administracion/', views.administracion, name='administracion'),
    path('error/', views.error_404, name='error'),
    path('alta_destinos', views.DestinosCreateView.as_view(), name="alta_destinos"),
    path('destinos_listado', views.DestinosListView.as_view(), name="destinos_listado"),
    path('contacto/mensajes_listado', views.mensajes_listado, name="mensajes_listado"),
    path('mostrar_destinos/', views.mostrar_destinos, name='mostrar_destinos'),
    path('mostrar_destinos/modificar_destino/<int:pk>', views.modificar_destino, name='modificar_destino'),
    path('mostrar_destinos/eliminar_destino/<int:pk>', views.eliminar_destino, name='eliminar_destino'),
]

