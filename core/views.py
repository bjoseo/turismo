   
    # finegap/views.py

from django.shortcuts import render, redirect
from .forms import SignupForm, ExcursiontravelForm, TravelForm
from django.http import HttpResponse
from .models import Contacto, Destinos, Travel, Excursiones, Excursiontravel
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import DestinosForm, ExcursionesForm


# pagina de inicio

def home(request):
    # user = int("{{ user.id }}")
    destinos = Destinos.objects.all()
    travel = Travel.objects.all()
    
    return render(request, 'core/home.html',{'destinos':destinos,'travel':travel})

# pagina para registrarse

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuario = User(username=usuario,email=email,password=password)
            usuario = form.save()
            usuario.set_password(usuario.password)
            try:
                usuario.save()
            except Exception as err:
                messages.error(request, " ocurrio un error ",err)
                return redirect('home')
            messages.info(request, "usuario dado de alta correctamente")
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

# pagina para enviar mensaje de contacto

def contacto(request):
   
    if request.method == 'POST':
            # from django.contrib.auth.models import User
            # user = User.objects.get(pk=user.id)

            # correo = user.email
            nombre = request.POST['name']
            apellido = request.POST['lastname']
            correo = request.POST['email']
            asunto = request.POST['subject']
            mensaje = request.POST['message']

            fecha = datetime.now()
            # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
            contacto = Contacto(name=nombre,lastname=apellido,email=correo,subject=asunto,message=mensaje,fecha=fecha)

            try:
                contacto.save()
            except Exception as err:
                messages.error(request, " ocurrio un error ",err)
                return redirect('contacto')
            
            messages.info(request, "mensaje enviado correctamente")
            return redirect('home')
    context = {
    }

    return render(request, 'core/contacto.html', context )

# listado de mensajes de contacto

def mensajes_listado(request):
    mensajes = Contacto.objects.all()
    ordering = ['name']
    return render(request,'core/mensajes_listado.html',{'mensajes':mensajes} )

# pagina acerca de nosotros

def acerca_de(request):
    return render(request, 'core/acerca_de.html')

# Opciones de Administracion

@login_required  

def administracion(request):
    context = {
    }
    return render(request,'core/administracion.html',context)

# Opcion Administracion CRUD tabla Destinos

@login_required  

def mostrar_destinos(request):
    destinos = Destinos.objects.all()
    return render(request,'core/mostrar_destinos.html',{'destinos':destinos} )

# alta Destinos

class DestinosCreateView(CreateView):
    model = Destinos
    request  = "files"
    template_name = 'core/alta_destinos.html'
    success_url = 'mostrar_destinos'
    fields = '__all__'

# modificar Destinos

def modificar_destino(request,pk):
    destinos = Destinos.objects.get(id=pk)
    if request.method == 'POST':
            destinos.Id = request.POST['Id']
            destinos.city = request.POST['city']
            destinos.country = request.POST['country']
            destinos.description = request.POST['description']
            destinos.urlImg = request.POST.get('urlImg')
            destinos.tipo = request.POST.get('tipo')

            try:
                destinos.save()   
            except Exception as err:
                messages.error(request, " ocurrio un error ",err)
                return redirect('mostrar_destinos')

            messages.info(request, "Se Modifico el Destino correctamente")
            return redirect('mostrar_destinos')
    context = {
            'destinos': destinos,
    }

    return render(request,'core/modificar_destino.html',context)

# eliminar Destinos

def eliminar_destino(request, pk):
    destinos = Destinos.objects.get(id=pk)
    if request.method == 'POST':
        try:
            destinos.delete()
        except Exception as err:
            messages.error(request, " ocurrio un error ",err)
            return redirect('mostrar_destinos')

        messages.info(request, "Se Elimino el Destino correctamente")
        return redirect('mostrar_destinos')

    context = {
        'destinos': destinos,
    }

    return render(request, 'core/eliminar_destino.html', context)

# Opcion Administracion CRUD tabla Excursiones

@login_required  

def mostrar_excursiones(request):
    excursiones = Excursiones.objects.all()
    return render(request,'core/mostrar_excursiones.html',{'excursiones':excursiones} )

# alta Excursion

class ExcursionesCreateView(CreateView):
    model = Excursiones
    request  = "files"
    template_name = 'core/alta_excursion.html'
    success_url = 'mostrar_excursiones'
    fields = '__all__'

# modificar Excursion

def modificar_excursion(request,pk):
    excursion = Excursiones.objects.get(id=pk)
    if request.method == 'POST':
            excursion.city = request.POST['city']
            excursion.description = request.POST['description']
            excursion.valor = request.POST.get('valor')
            excursion.tipo = request.POST.get('tipo')
            try:
                excursion.save()   
            except Exception as err:
                messages.error(request, " ocurrio un error ",err)
                return redirect('mostrar_excursiones')

            messages.info(request, "Se Modifico la Excursion correctamente")
            return redirect('mostrar_excursiones')
    context = {
            'excursion': excursion,
    }

    return render(request,'core/modificar_excursion.html',context)

# eliminar Excursion

def eliminar_excursion(request, pk):
    excursion = Excursiones.objects.get(id=pk)
    if request.method == 'POST':
        try:
            excursion.delete()
        except Exception as err:
            messages.error(request, " ocurrio un error ",err)
            return redirect('mostrar_excursiones')

        messages.info(request, "Se Elimino la Excursion correctamente")
        return redirect('mostrar_excursiones')

    context = {
        'excursion': excursion,
    }

    return render(request, 'core/eliminar_excursion.html', context)

# Listado de  Paquetes

def travel_list(request):
    travels = Travel.objects.all()
    return render(request, 'travel/travel_list.html', {'travels': travels})

# detalle Paquete para usuario

def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    return render(request, 'travel/travel_detail.html', {'travel': travel})

# detalle Paquetes para administrador

def travel_detail_admin(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    return render(request, 'travel/travel_detail_admin.html', {'travel': travel})

# crear Paquete

def travel_new(request):
    if request.method == "POST":
        form = TravelForm(request.POST)
        excursiontravel_form = ExcursiontravelForm(request.POST)
        if form.is_valid() and excursiontravel_form.is_valid():
            travel = form.save(commit=False)
            travel.save()
            excursiontravel = excursiontravel_form.save(commit=False)
            excursiontravel.save()
            return redirect('travel_detail', pk=travel.pk)
    else:
        form = TravelForm()
    return render(request, 'travel/travel_edit.html', {'form': form})

# editar Paquete

def travel_edit(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if request.method == "POST":
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.save()
            return redirect('travel_list')
    else:
        form = TravelForm(instance=travel)
    return render(request, 'travel/travel_edit.html', {'form': form})

# eliminar Paquete

def travel_delete(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if request.method == 'POST':
        try:
            travel.delete()
        except Exception as err:
            messages.error(request, " ocurrio un error ",err)
            return redirect('mostrar_excursiones')

        messages.info(request, "Se Elimino la Excursion correctamente")
        return redirect('travel_list')

    context = {
        'travel': travel,
    }

    return render(request, 'travel/travel_delete.html', context)

# pagina de error

def error_404(request):
    context = {
    }
    return render(request, "core/error_404.html", context)

