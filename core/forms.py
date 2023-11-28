# forms.py

from django import forms
from .models import Destinos, Excursiontravel, Excursiones, Travel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# formulario para dar de alta un usuario

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# formulario para dar de alta un destino

class AltaDestinos(forms.ModelForm):
    class Meta:
        model = Destinos
        fields = '__all__'


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['destino', 'fecha_desde', 'fecha_hasta', 'valor', 'pasajeros', 'usuarios', 'excursiones']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Excluye usuario admin
        self.fields['destino'].queryset = Destinos.objects.exclude(tipo=3)
    
        # Excluye usuario admin
        self.fields['usuarios'].queryset = User.objects.exclude(id=1)

class DestinosForm(forms.ModelForm):
    class Meta:
        model = Destinos
        fields = ['Id', 'city', 'country', 'description', 'urlImg', 'tipo']

class ExcursionesForm(forms.ModelForm):
    class Meta:
        model = Excursiones
        fields = ['city', 'description', 'valor', 'tipo']

class ExcursiontravelForm(forms.ModelForm):
    class Meta:
        model = Excursiontravel
        fields = ['travel', 'excursiones']
