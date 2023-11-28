# finegap/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/signup/',views.signup, name="signup"),
   
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/mensajes_listado', views.mensajes_listado, name="mensajes_listado"),

    path('acerca_de/', views.acerca_de, name='acerca_de'),

    path('administracion/', views.administracion, name='administracion'),

    path('mostrar_destinos/', views.mostrar_destinos, name='mostrar_destinos'),
    path('alta_destinos', views.DestinosCreateView.as_view(), name="alta_destinos"),
    path('mostrar_destinos/modificar_destino/<int:pk>', views.modificar_destino, name='modificar_destino'),
    path('mostrar_destinos/eliminar_destino/<int:pk>', views.eliminar_destino, name='eliminar_destino'),

    path('mostrar_excursiones/', views.mostrar_excursiones, name='mostrar_excursiones'),
    path('alta_excursion', views.ExcursionesCreateView.as_view(), name="alta_excursion"),
    path('mostrar_excursiones/modificar_excursion/<int:pk>', views.modificar_excursion, name='modificar_excursion'),
    path('mostrar_excursiones/eliminar_excursion/<int:pk>', views.eliminar_excursion, name='eliminar_excursion'),
   
    path('travels/', views.travel_list, name='travel_list'),
    path('travel/<int:pk>/', views.travel_detail, name='travel_detail'),
    path('travel/travel_detail_admin/<int:pk>/', views.travel_detail_admin, name='travel_detail_admin'),
    path('travel/travel_new/', views.travel_new, name='travel_new'),
    path('travel/travel_edit/<int:pk>', views.travel_edit, name='travel_edit'),
    path('travel/<int:pk>/delete/', views.travel_delete, name='travel_delete'),

    path('error/', views.error_404, name='error'),

]

