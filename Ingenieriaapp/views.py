from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from collections import UserString
#from django.contrib.auth.models import Usuario
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.hashers import make_password
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
#import requests
from django.http import HttpResponse
from PIL import Image
from io import BytesIO



# Create your views here.

#Login

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    message = ''
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_administrador:
            print("is_administrador")
            return redirect('/ControladorVideojuegos/')
        else:
            print("es un usuario común")
            return redirect('/Usuario/')
    else:
        messages.add_message(request , messages.INFO, 'Usuario no Válido' )
        return render(request, "autenticar.html", {'message':message})
   
def logout_user(request):
    logout(request)
    return render(request, "autenticar.html")

def registro(request):
    if request.method == 'POST':
        form = userform(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = Usuario.objects.create_user(username=username)

            user.set_password(password)
            user.save()

            messages.success(request, "Te has registrado correctamente")    
            return redirect('/Usuario/')
    else:
        form = userform()

    context = {'form': form}
    return render(request, 'registro.html', context)


#Admin

def ControladorVideojuegos (request):
    busqueda = request.GET.get("buscar")
    videojuegos = Videojuegos.objects.all()
    data = {'videojuegos': videojuegos}
    if busqueda:
            videojuegos = Videojuegos.objects.filter(
           
            Q(nombre__icontains = busqueda) |
            Q(descripcion = busqueda)
             

         ).distinct()
    return render(request, "ListaVideojuegos.html", {'videojuegos': videojuegos})

def anadir_juego (request):
    
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        foto = request.FILES['foto']

        app =Videojuegos(nombre=nombre, descripcion=descripcion, foto=foto)
        app.save()
        return redirect('/ControladorVideojuegos/')
    else:
        return render(request, 'añadir_juego.html')

        

def ControladorSolicitud (request):
    busqueda = request.GET.get("buscar")
    solicitud = Solicitud.objects.all()
    data = {'solicitud': solicitud}
    if busqueda:
            solicitud = Solicitud.objects.filter(
            
            Q(nombreapp__icontains = busqueda)
            

         ).distinct()

    return render(request, "ListaSolicitudes.html", {'solicitud':solicitud})

def denegar_solic(request, solicitud_id):
    try:
        Solicitud.objects.get(id=solicitud_id).delete()
    except Solicitud.DoesNotExist:
        pass
    return redirect('/ControladorSolicitud')

def aceptar_solic(request, solicitud_id):
    usuario = Solicitud.objects.get(id=solicitud_id)
    if request.method == 'POST':
        usuario = Solicitud.objects.get(id=solicitud_id)
        
        return redirect ('/ControladorSolicitud/')

def GenerarReport (request):
    return render (request, 'GenerarReport.html')

def ControladorUsuario (request):
    busqueda = request.GET.get("buscar")
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    if busqueda:
            usuarios = Usuario.objects.filter(
           Q(first_name__icontains = busqueda) |
            Q(last_name__icontains = busqueda) |
            Q(username__icontains = busqueda) 

         ).distinct()

    return render(request, "ListaUsuario.html", {'usuarios':usuarios})
    #return render (request, 'ControladorUsuario.html')

def delete_usuario(request, usuario_id):
    try:
        Usuario.objects.get(id=usuario_id).delete()
    except Usuario.DoesNotExist:
        pass
    return redirect('/ControladorUsuario/')

def modificar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        usuario.username = request.POST['usuario']
        usuario.first_name = request.POST['nombre']
        usuario.last_name = request.POST['apellidos']
        usuario.is_administrador = request.POST['is_administrador']

        if request.POST.get('contraseña'):
            usuario.password = make_password(request.POST['contraseña'])
        usuario.save()

        

        data = {
            'usuario': Usuario.objects.all()
        }
        
        return redirect('/ControladorUsuario/')

    else:
        return render(request, "modificar_usuario.html", {'usuario':usuario})
    
    
def delete_videojuego(request, videojuego_id):
    try:
        Videojuegos.objects.get(id=videojuego_id).delete()
    except Videojuegos.DoesNotExist:
        pass
    return redirect('/ControladorVideojuegos/')

def descargar_videojuego (request, videojuego_id):
    # Recuperar la imagen desde la base de datos
    image = Videojuegos.objects.get(id=videojuego_id).foto

    # Abrir la imagen con PIL
    pil_image = Image.open(BytesIO(image))

    # Convertir la imagen a bytes
    image_bytes = BytesIO()
    pil_image.save(image_bytes, format='JPEG')

    # Crear la respuesta HTTP con la imagen
    response = HttpResponse(image_bytes.getvalue(), content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename="image.jpg"'
    return response
    
def opcion (request):
    user = request.usuario
    if user is not None:
        if user.is_administrador:
            print("is_administrador")
            return redirect('/listaVideojuegos/')
        
        
        else:
            return render (request, "Usuario.html")

#Usuario

def principal (request):
    return render (request, 'autenticar.html')

def usuario (request):
    busqueda = request.GET.get("buscar")
    aplicaciones = Videojuegos.objects.all()
    data = {'aplicaciones': aplicaciones}
    if busqueda:
            aplicaciones = Videojuegos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion = busqueda)
             

         ).distinct()
    return render(request, "Usuario.html", {'aplicaciones':aplicaciones})
    



def descargar (request, aplicacion_id): 
    imagen = get_object_or_404(Videojuegos, id=aplicacion_id)
    response = HttpResponse(imagen.imagen, content_type=imagen.tipo)
    response['Content-Disposition'] = f'attachment; filename=foto{id}.{imagen.tipo}'
    return response

def solicitud (request):
    if request.method == 'POST':
        nombreapp = request.POST['nombreapp']
        
        solic =Solicitud(nombreapp=nombreapp)
        solic.save()
        return redirect('/Usuario/')
    else:
       
        return render (request, 'solicitud.html')


def ControladorComentarios(request, videojuegos_id):
    videojuegos = get_object_or_404(Videojuegos, pk=videojuegos_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.videojuegos = videojuegos
            comentario.save()
            return redirect('detalle_videojuego', videojuego_id=videojuego.id)
    else:
        form = ComentarioForm()
    return render(request, 'agregar_comentario.html', {'form': form})
