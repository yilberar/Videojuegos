from django.test import TestCase
from .models import Usuario
from  .models import Videojuegos
from .models import Usuario, Solicitud

class UsuarioTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            username="testuser",
            password="testpassword",
          
           
        )

    def test_model_can_Autenticar_usuario(self):
        old_count = Usuario.objects.count()
        new_usuario = Usuario.objects.create(
            username="yilberar",
            password="yilber051235",
          
           
        )
        new_count = Usuario.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_usuario.username, "yilberar")
        self.assertEqual(new_usuario.password, "yilber051235")
     





class SolicitudTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            username="testuser",
            password="testpassword",
        )
        self.solicitud = Solicitud.objects.create(
            autor=self.usuario,
            nombreapp="Hola",
        )

    def test_model_can_create_solicitud(self):
        old_count = Solicitud.objects.count()
        new_solicitud = Solicitud.objects.create(
            autor=self.usuario,
            nombreapp="Hola",
        )
        new_count = Solicitud.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_solicitud.nombreapp, "Hola")





       
