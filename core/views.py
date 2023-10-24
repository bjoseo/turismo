   
    # finegap/views.py

from django.shortcuts import render, redirect
from .forms import Formulariocontacto, FormularioUsuario
from .models import Usuario
from .models import FormContacto, Destinos
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db import IntegrityError
from django.contrib import messages
from tkinter import messagebox as MessageBox

def home(request):
    return render(request, 'core/home.html')

def login(request):
    context = {
    }
    return render(request, "core/login.html", context)

def Create_Usuario(request):
    if request.method == 'POST':
        Create_Usuario_form = FormularioUsuario(request.POST)
        if Create_Usuario_form.is_valid():
            # Procesar el formulario si es válido
            nombre = Create_Usuario_form.cleaned_data['name']
            correo = Create_Usuario_form.cleaned_data['email']
            password = Create_Usuario_form.cleaned_data['password']
            # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
            usuario = Usuario(name=nombre,email=correo,password=password)

            try:
                usuario.save()
            except Exception as ie:
                messages.error(request, " ocurrio un error ")

            messages.info(request, "Usuario dado de alta correctamente")
            return redirect(reverse("home"))
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        Create_Usuario_form = FormularioUsuario()

    return render(request, 'core/CreateUsuario.html', {'form': Create_Usuario_form})


def contacto(request):
    if request.method == 'POST':
        form = Formulariocontacto(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            nombre = form.cleaned_data['name']
            apellido = form.cleaned_data['lastname']
            correo = form.cleaned_data['email']
            asunto = form.cleaned_data['subject']
            mensaje = form.cleaned_data['message']
            # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
            contacto = FormContacto(name=nombre,lastname=apellido,email=correo,subject=asunto,message=mensaje)

            try:
                contacto.save()

            except Exception as ie:
                messages.error(request, " ocurrio un error ")

            messages.info(request, "Mensaje dado de alta correctamente")
            return redirect(reverse("home"))
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        form = Formulariocontacto()

    return render(request, 'core/contacto.html', {'form': form})


def acerca_de(request):
    return render(request, 'core/acerca_de.html')

def administracion(request):
     return render(request, "core/administracion.html")

def destinos(request, destino):
     return render(request, "core/destinos.html", {
        "destino": destino
    })

def error_404(request):
    context = {
    }
    return render(request, "core/error_404.html", context)

# alta Destinos

class DestinosCreateView(CreateView):
    model = Destinos
    request  = "files"
    template_name = 'core/alta_destinos.html'
    success_url = 'mostrar_destinos'
    fields = '__all__'


class DestinosListView(ListView):
    model = Destinos
    context_object_name = 'listado_destinos'
    template_name = 'core/destinos_listado.html'
    ordering = ['tipo']

class MensajesListView(ListView):
    model = FormContacto
    context_object_name = 'listado_mensajes'
    template_name = 'core/mensajes_listado.html'
    ordering = ['name']

def mensajes_listado(request):
    mensajes = FormContacto.objects.all()
    ordering = ['name']
    return render(request,'core/mensajes_listado.html',{'mensajes':mensajes} )



# recuperar Destinos
        
def mostrar_destinos(request):
    destinos = Destinos.objects.all()
    ordering = ['city']
    return render(request,'core/mostrar_destinos.html',{'destinos':destinos} )




# modificar Destinos

def modificar_destino(request,pk):
    destinos = Destinos.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        destinos.Id = request.POST['Id']
        destinos.city = request.POST['city']
        destinos.country = request.POST['country']
        destinos.description = request.POST['description']
        destinos.urlImg = request.POST['urlImg']
        destinos.activo = request.POST['activo']
        destinos.tipo = request.POST['tipo']
        try:
            destinos.save()   
        except Exception as ie:
            messages.error(request, " ocurrio un error ")

        messages.info(request, "Se Modifico el Destino correctamente")
        return redirect('mostrar_destinos')
    context = {
        'destinos': destinos,
    }

    return render(request,'core/modificar_destino.html',context)

# eliminar Destinos


def eliminar_destino(request, pk):
    destinos = Destinos.objects.get(id=pk)
    print(request.POST)
    if request.method == 'POST':
        try:
            destinos.delete()
        except Exception as ie:
            messages.error(request, " ocurrio un error ")

        messages.info(request, "Se Elimino el Destino correctamente")
        return redirect('mostrar_destinos')

    context = {
        'destinos': destinos,
    }

    return render(request, 'core/eliminar_destino.html', context)