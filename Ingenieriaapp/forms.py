from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelChoiceField, ModelForm
from Ingenieriaapp.models import  *
from django.contrib.auth.forms import UserCreationForm

class userform (ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    class Meta :
        model = Usuario
        fields = ['username', 'password', 'password1']

class CustomUserCreationForm (UserCreationForm):
    pass

class DescargarFotoForm(forms.Form):
    url = forms.URLField(label='Enlace de descarga')

class aplicacionesform (ModelForm):
    foto = forms.ImageField(label="Imagen", widget=forms.FileInput)
    class Meta :
        model = Videojuegos
        fields = ['nombre', 'descripcion', 'foto']

class solicitudform (ModelForm):
    
        model = Solicitud
        fields = ['username', 'password', 'password1']