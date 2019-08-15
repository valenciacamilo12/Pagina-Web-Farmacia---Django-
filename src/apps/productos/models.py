from django.db import models
from apps.empleados.models import Empleado
from apps.clientes.models import Cliente
from django.utils.translation import ugettext as _


class Categoria(models.Model):
    cod_cate = models.AutoField(primary_key=True, unique=True)
    nom_cate = models.CharField(max_length = 20)


class Presentacion(models.Model):
    cod_prese = models.AutoField(primary_key=True, unique=True)
    nom_pre = models.CharField(max_length = 20)



class Distrito(models.Model):
    cod_dis = models.AutoField(primary_key=True,unique=True)
    nom_dis = models.CharField(max_length = 20)
    empleado = models.ForeignKey(Empleado,models.CASCADE,null=True,blank=True)

class Proveedor(models.Model):
    cod_proveedor = models.AutoField(primary_key=True,unique=True)
    nom_prov = models.CharField(max_length=20)
    dr_prov = models.CharField(max_length=20)
    telefono = models.IntegerField(10)
    celular = models.IntegerField(10)
    id_distrito = models.ForeignKey(Distrito, models.CASCADE, null=True, blank=True)



class Producto(models.Model):
    cod_producto = models.AutoField(primary_key=True,unique=True)
    nom_producto = models.CharField(max_length=30)
    pre_venta = models.CharField(max_length=30)
    pre_compra = models.CharField(max_length=30)
    fecha_ven = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    producto_imagen = models.ImageField(blank=True, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    cod_cate = models.ForeignKey(Categoria, models.CASCADE, blank=True, null=True)
    cod_prove = models.ForeignKey(Proveedor, models.CASCADE, blank=True, null=True)
    cod_pres = models.ForeignKey(Presentacion, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nom_producto)

    class Meta:
        permissions = {
            ('is_uno', _('Usuario Uno')),
            ('is_dos', _('Usuario Dos')),
        }



class DetalleOrdenPedido(models.Model):
    cod_pro = models.ForeignKey(Producto, models.CASCADE, null=True, blank=True)
    nom_pro = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio_venta = models.CharField(max_length=20)
    importe = models.CharField(max_length=20)



class OrdenPedido(models.Model):
    num_ordenpedido = models.AutoField(primary_key=True,unique=True)
    fecha = models.CharField(max_length=20)
    codigo_cliente = models.ForeignKey(Cliente, models.CASCADE, null=True, blank=True)
    nombre_cliente = models.CharField(max_length=30,default=True)
    cod_tipopago = models.CharField(max_length=30)
    total = models.CharField(max_length=30)




class Boleta(models.Model):
    num_boleta = models.AutoField(primary_key = True, unique=True)
    fecha = models.CharField(max_length=10)
    codi_empl = models.ForeignKey(Empleado, models.CASCADE,null=True,blank=True)
    codi_cli = models.ForeignKey(Cliente, models.CASCADE, null=True, blank=True)
    num_ordenpedido = models.ForeignKey(OrdenPedido,models.CASCADE, null=True, blank=True)
    subtotal = models.CharField(max_length=30)
    descuento = models.CharField(max_length=30)

