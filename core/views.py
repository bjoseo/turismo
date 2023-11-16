   
    # finegap/views.py

from django.shortcuts import render, redirect
from .forms import Formulariocontacto, FormularioUsuario
from django.http import HttpResponse
from .models import Contacto, Destinos, Travel
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# pagina de inicio

def home(request):
    request.session['user_name'] = "{{user.username}}"
    request.session['user_last_name'] = "{{user.last_name}}"
    request.session['usuario'] = "{{user.id}}"
    destinos = Destinos.objects.all()
    # return render(request,'core/mostrar_destinos.html',{'destinos':destinos} )

    return render(request, 'core/home.html',{'destinos':destinos})

# pagina para login

# def login(request):
#     context = {
#     }
#     return render(request, "core/login.html", context)

# opcion para crear usuario

def create_usuario(request):
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        # if form.is_valid():
        #     # Procesar el formulario si es válido
        #     nombre = form.cleaned_data['name']
        #     correo = form.cleaned_data['email']
        #     password = form.cleaned_data['password']
        #     # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
        #     # usuario = Usuario(name=nombre,email=correo,password=password)

        #     try:
        #         usuario.save()
        #     except Exception as err:
        #         messages.error(request, " ocurrio un error ",err)
        #         return redirect(reverse("login"))

        #     messages.info(request, "Usuario dado de alta correctamente")
        #     return redirect(reverse("home"))
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        form = FormularioUsuario()

    return render(request, 'core/create_usuario.html', {'form': form})



# pagina para enviar mensaje de contacto

def contacto(request):
    user_name = request.session['user_name']
    user_last_name = request.session['user_last_name']
    # user_id = request.session['usuario']
    
    context = {
        'user_name' : user_name,
        'user_last_name' : user_last_name,
        # 'user_id' : user_id
    }

    if request.method == 'POST':
        form = Formulariocontacto(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            nombre = form.cleaned_data['name']
            apellido = form.cleaned_data['lastname']
            correo = form.cleaned_data['email']
            asunto = form.cleaned_data['subject']
            mensaje = form.cleaned_data['message']

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
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        form = Formulariocontacto()

    return render(request, 'core/contacto.html', {'form': form})

# listado de mensajes de contacto

def mensajes_listado(request):
    mensajes = Contacto.objects.all()
    ordering = ['name']
    return render(request,'core/mensajes_listado.html',{'mensajes':mensajes} )



# pagina acerca de nosotros

def acerca_de(request):
    return render(request, 'core/acerca_de.html')

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
            Destinos.Id = request.POST['Id']
            Destinos.city = request.POST['city']
            Destinos.country = request.POST['country']
            Destinos.description = request.POST['description']
            Destinos.urlImg = request.POST.get('urlImg')
            Destinos.tipo = request.POST.get('tipo')
            try:
                Destinos.save()   
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

# alta Travel

def alta_travel(request,pk):
    destinos = Destinos.objects.get(id=pk)
    if request.method == 'POST':
            Destinos.Id = request.POST['Id']
            Destinos.city = request.POST['city']
            Destinos.country = request.POST['country']
            Destinos.description = request.POST['description']
            Destinos.urlImg = request.POST.get('urlImg')
            Destinos.tipo = request.POST.get('tipo')
            try:
                Destinos.save()   
            except Exception as err:
                messages.error(request, " ocurrio un error ",err)
                return redirect('mostrar_destinos')

            messages.info(request, "Se Modifico el Destino correctamente")
            return redirect('mostrar_destinos')
    context = {
            'destinos': destinos,
    }

    return render(request,'core/alta_travel.html',context)


# class TravelCreateView(CreateView):
#     model = Destinos
#     # model1 = Travel
#     request  = "files"
#     template_name = 'core/alta_travel.html'
#     success_url = 'home'
#     fields = '__all__'

# pagina de error 404

def error_404(request):
    context = {
    }
    return render(request, "core/error_404.html", context)


# def modificar_destino(request, pk):
#     destinos = Destinos.objects.get(id=pk)
#     if request.method == "POST":
#         form = DestinoForm(request.POST, request.FILES, instance=destinos)
#         if form.is_valid():
#             destinos = form.save(commit=False)
#             destinos.save()
            
#             messages.info(request, "Se Modifico el Destino correctamente")

#             return redirect(reverse("mostrar_destinos"))
#     else:
#         form = DestinoForm(instance=destinos)
#     return render(request, 'core/modificar_destino.html', {'form': form})





# class DestinosListView(LoginRequiredMixin,ListView):
#     model = Destinos
#     context_object_name = 'destinos'
#     template_name = 'core/destinos_listado.html'
#     ordering = ['tipo']

# class MensajesListView(LoginRequiredMixin,ListView):
#     model = Contacto
#     context_object_name = 'listado_mensajes'
#     template_name = 'core/mensajes_listado.html'
#     ordering = ['name']

# Recuperar un Usuario

# def read_usuario(request,pk):
#     try:
#         destinos = Usuario.objects.get(id=pk)
#     except Exception as err:
#         messages.error(request, " no exixte ",err)
#         return
            
#     messages.info(request, "si existe")
#     return

    # return (usuario.email)

    # return render(request, 'core/contacto.html', {'form': form}, context = context)
