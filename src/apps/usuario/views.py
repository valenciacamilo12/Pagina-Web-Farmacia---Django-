from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.models import User
from apps.usuario.forms import RegistroForm
from django.core.urlresolvers import reverse_lazy
from apps.productos.models import Producto

class RegistrarUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuarios/registrar.html'
    success_url = reverse_lazy('usuarios:usuarios_inicio')


class UsuarioInicio(ListView):
    model = Producto
    template_name = 'productos/index.html'


