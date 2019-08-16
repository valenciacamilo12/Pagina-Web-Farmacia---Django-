from django.conf.urls import url
from apps.productos.views import CreateProducto,ListProducto,DetailViewProducto,UpdateProducto,DeleteProducto
from apps.productos.views import CreateCategoria, ListCategoria, UpdateCategoria, DeleteCategoria

urlpatterns = [
    url(r'^nuevo$', CreateProducto.as_view(), name = 'producto_create'),
    url(r'^listar$', ListProducto.as_view(), name = 'producto_listar'),
    url(r'^detalle/(?P<pk>\d+)$', DetailViewProducto.as_view(), name='producto_detalle'),
    url(r'^editar/(?P<pk>[\d]+)/$', UpdateProducto.as_view(), name='producto_editar'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', DeleteProducto.as_view(), name='producto_eliminar'),
    url(r'^categoria/nueva$', CreateCategoria.as_view(), name='categoria_nueva'),
    url(r'^categorias/listar$', ListCategoria.as_view(), name='categoria_listar'),
    url(r'^editar/categoria/(?P<pk>[\d]+)/$', UpdateCategoria.as_view(), name='categoria_editar'),
    url(r'^eliminar/categoria/(?P<pk>[\d]+)/$', DeleteCategoria.as_view(), name='categoria_eliminar'),
]