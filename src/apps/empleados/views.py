from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.productos.models import Producto
from apps.productos.forms import ProductoForm


class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('empleados:producto_listar')


class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('empleados:producto_listar')


class DeleteProducto(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'empleados/producto_delete.html'
    success_url = reverse_lazy('empleados:producto_listar')


class ListProduct(ListView):
    model = Producto
    template_name = 'empleados/producto_list.html'