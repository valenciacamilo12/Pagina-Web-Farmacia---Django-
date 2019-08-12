from django.conf.urls import url
from apps.productos.views import index,CreateProducto,ListProducto

urlpatterns = [
    url(r'^$', index),
    url(r'^nuevo$', CreateProducto.as_view(), name = 'producto_create'),
    url(r'^listar$', ListProducto.as_view(), name = 'producto_listar'),
]