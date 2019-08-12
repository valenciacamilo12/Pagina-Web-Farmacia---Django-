from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from apps.productos.models import Producto
from apps.productos.forms import ProductoForm
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request, 'productos/index.html')


class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class ListProducto(ListView):
    model = Producto
    template_name = 'productos/producto_shop.html'