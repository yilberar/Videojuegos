from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.


class Usuario(AbstractUser):
    CI = models.CharField(_("CI"),max_length=12)
    is_administrador = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name + self.last_name + self.username 
       
class Videojuegos (models.Model):
    autor = models.ForeignKey("Ingenieriaapp.Usuario", on_delete=models.SET_NULL,null=True, related_name='Videojuegos')
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150)
    foto = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.nombre + self.foto
    
class Solicitud (models.Model):
    autor = models.ForeignKey("Ingenieriaapp.Usuario", on_delete=models.SET_NULL,null=True, related_name='Solicitud')
    nombreapp = models.CharField(max_length=50)
    
    def __str__(self):
        return self.autor + self.nombreapp 


class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)