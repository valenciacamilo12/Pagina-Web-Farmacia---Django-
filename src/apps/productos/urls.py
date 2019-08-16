from django.conf.urls import url
from apps.productos.views import CreateProducto,ListProducto,DetailViewProducto,UpdateProducto,DeleteProducto
from apps.productos.views import CreateCategoria, ListCategoria, UpdateCategoria, DeleteCategoria
from apps.productos.views import CreatePresentacion, ListPresentacion, UpdatePresentacion, DeletePresentacion
from apps.productos.views import CreateDistrito, ListDistrito, UpdateDistrito, DeleteDistrito

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
    url(r'^presentacion/nueva$', CreatePresentacion.as_view(), name='presentacion_nueva'),
    url(r'^presentacion/listar$', ListPresentacion.as_view(), name='presentacion_listar'),
    url(r'^editar/presentacion/(?P<pk>[\d]+)/$', UpdatePresentacion.as_view(), name='presentacion_editar'),
    url(r'^eliminar/presentacion/(?P<pk>[\d]+)/$', DeletePresentacion.as_view(), name='presentacion_eliminar'),
    url(r'^distrito/nuevo$', CreateDistrito.as_view(), name='distrito_nuevo'),
    url(r'^distrito/listar$', ListDistrito.as_view(), name='distrito_listar'),
    url(r'^distrito/editar/(?P<pk>[\d]+)/$', UpdateDistrito.as_view(), name='distrito_editar'),
    url(r'^distrito/eliminar/(?P<pk>[\d]+)/$', DeleteDistrito.as_view(), name='distrito_eliminar'),
]