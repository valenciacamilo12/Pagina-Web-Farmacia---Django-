from django.conf.urls import url
from apps.usuario.views import RegistrarUsuario,UsuarioInicio

urlpatterns = [
    url(r'^registrar', RegistrarUsuario.as_view(), name = 'registrar'),
    url(r'^inicio', UsuarioInicio.as_view(), name = 'usuarios_inicio'),
]