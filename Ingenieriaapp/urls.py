from re import template 
from django.urls import path
from unicodedata import name
#from django.contrib.auth.views import loginView, LogoutView
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from django.contrib.auth import views
from django.contrib.auth import views as auth_view
from Ingenieriaapp import views
from Ingenieriaapp.views import *



app_name = "Ingenieriaapp"


urlpatterns= [
   path('',views.principal, name="autenticar"), 
   path('login_user/',views.login_user, name="login_user"),
   #path('login_user/',LoginView.as_view(template_name = 'autenticar.html'), name="login_user"),
   path('logout_user/',views.logout_user, name="logout_user"),
   #path('logout_user/',LogoutView.as_view(template_name = 'autenticar.html'), name="logout_user"),
   path('Usuario/', usuario, name="usuario"),
   path('registro/', registro, name="registro"),
   path('solicitud/', solicitud, name="solicitud"),

                    #Admin
   path('anadir_juego/', anadir_juego, name="anadir_juego"),
   path('ControladorSolicitud/', ControladorSolicitud, name="ControladorSolicitud"),
   path('ControladorSolicitud/<int:solicitud_id>/denegar/',views.denegar_solic, name="denegar_solic"),
   path('denegar_solic/<int:solicitud_id>',views.denegar_solic, name="denegar_solic"),
   path('aceptar_solic/<int:solicitud_id>', views.aceptar_solic, name = "aceptar_solic"),
   path('ControladorSolicitud/<int:solicitud_id>/aceptar/',views.aceptar_solic, name="aceptar_solic"),

   path('GenerarReport/', GenerarReport, name="GenerarReport"),

   path('ControladorUsuario/', ControladorUsuario, name="ControladorUsuario"),
   path('ControladorUsuario/<int:usuario_id>/delete/',views.delete_usuario, name="delete_usuario"),
   path('delete_usuario/<int:usuario_id>',views.delete_usuario, name="delete_usuario"),
   path('modificar_usuario/<int:usuario_id>', views.modificar_usuario, name = "modificar_usuario"),
   path('ControladorUsuario/<int:usuario_id>/modificar/',views.modificar_usuario, name="modificar_usuario"),
   
   path('ControladorVideojuegos/', ControladorVideojuegos, name="ControladorVideojuegos"),
   path('ControladorVideojuegos/<int:videojuego_id>/delete/',views.delete_videojuego, name="delete_videojuego"),
   path('delete_videojuego/<int:videojuego_id>',views.delete_videojuego, name="delete_videojuego"),

   path('ControladorVideojuegos/<int:videojuego_id>/',views.descargar_videojuego, name="descargar_videojuego"),
   path('descargar_videojuego/<int:videojuego_id>',views.descargar_videojuego, name="descargar_videojuego"),

   ]

