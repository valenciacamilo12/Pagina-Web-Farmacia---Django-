from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from apps.productos.models import Producto
from apps.productos.models import Categoria
from apps.productos.forms import ProductoForm
from apps.productos.forms import CategoriaForm
from apps.productos.forms import PresentacionForm
from apps.productos.forms import DistritoForm
from apps.productos.forms import ProveedorForm
from django.core.urlresolvers import reverse_lazy

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class ListProducto(ListView):
    model = Producto
    template_name = 'productos/producto_shop.html'


class DetailViewProducto(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'


class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class DeleteProducto(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('productos:producto_listar')




#-----------------Categoria--------------------------------------------------

class ListCategoria(ListView):
    model = Categoria
    template_name = 'productos/categoria_list.html'


class UpdateCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class DeleteCategoria(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_delete.html'
    success_url = reverse_lazy('productos:producto_listar')



class CreateCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_form.html'
    success_url = reverse_lazy('productos:producto_listar')
