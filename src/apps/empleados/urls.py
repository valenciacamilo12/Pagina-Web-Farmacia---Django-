from django.conf.urls import url
from apps.empleados.views import CreateProducto,UpdateProducto,DeleteProducto,ListProduct
urlpatterns = [
    url(r'^producto/listar$', ListProduct.as_view(), name='producto_listar'),
    url(r'^producto/nuevo$', CreateProducto.as_view(), name='producto_nuevo'),
    url(r'^producto/editar/(?P<pk>[\d]+)/$', UpdateProducto.as_view(), name='producto_editar'),
    url(r'^producto/eliminar/(?P<pk>[\d]+)/$', DeleteProducto.as_view(), name='producto_eliminar'),
]