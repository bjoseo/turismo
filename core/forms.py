# forms.py

from django import forms
from .models import Destinos

class Formulariocontacto(forms.Form):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'id':'fname','class':'estilo_input','placeholder':'Nombre','autocomplete':'off'}), max_length=20 ,required=True)
    lastname = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'id':'fapell','class':'estilo_input','placeholder':'Apellido'}), max_length=20 ,required=True)
    email = forms.EmailField(label='Correo electrónico', widget=forms.TextInput(attrs={'id':'fmail','class':'estilo_input','placeholder':'Correo electrónico','autocomplete':'off'}), max_length=100 ,required=True)
    subject = forms.CharField(label='Asunto', widget=forms.TextInput(attrs={'id':'fasunto','class':'estilo_input','placeholder':'Asunto'}), max_length=200 ,required=True)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'id':'fmsg','rows':'3', 'cols':'20','placeholder':'Envíenos sus comentarios'}), max_length=500)


class FormularioUsuario(forms.Form):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'id':'fname','class':'estilo_input','placeholder':'Nombre','autocomplete':'off'}), max_length=20 ,required=True)
    email = forms.EmailField(label='Correo electrónico', widget=forms.TextInput(attrs={'id':'fmail','class':'estilo_input','placeholder':'Correo electrónico','autocomplete':'off'}), max_length=20 ,required=True)
    password = forms.CharField(label='password', widget=forms.TextInput(attrs={'id':'fpassword','class':'estilo_input','placeholder':'Contraseña'}), max_length=100 ,required=True)

class AltaDestinos(forms.ModelForm):
    class Meta:
        model = Destinos
        fields = '__all__'
