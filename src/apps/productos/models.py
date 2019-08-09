from django.db import models

# Falta hacer la relacion entre las tablas OrdenPedido,Clientes,Empleados


class Categoria(models.Model):
    cod_cate = models.AutoField(primary_key=True,unique=True)
    nom_cate = models.CharField(max_length = 20)


class Presentacion(models.Model):
    cod_prese = models.AutoField(primary_key=True,unique=True)
    nom_pre = models.CharField(max_length = 20)



class Distrito(models.Model):
    cod_dis = models.AutoField(primary_key=True,unique=True)
    nom_dis = models.CharField(max_length = 20)


class Proveedor(models.Model):
    cod_proveedor = models.AutoField(primary_key=True,unique=True)
    nom_prov = models.CharField(max_length = 20)
    dr_prov = models.CharField(max_length = 20)
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
    cod_cate = models.ForeignKey(Categoria, models.CASCADE, blank=True, null=True)
    cod_prove = models.ForeignKey(Proveedor, models.CASCADE, blank=True, null=True)
    cod_pres = models.ForeignKey(Presentacion, models.CASCADE, blank=True, null=True)


class DetalleOrdenPedido(models.Model):
    cod_pro = models.ForeignKey(Producto, models.CASCADE, null=True, blank=True)
    nom_pro = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio_venta = models.CharField(max_length=20)
    importe = models.CharField(max_length=20)



class OrdenPedido(models.Model):
    num_ordenpedido = models.AutoField(primary_key=True,unique=True)
    fecha = models.CharField(max_length=20)
    #codigo_cliente = models.ForeignKey()
    #nombre_cliente = models.ForeignKey()
    cod_tipopago = models.CharField(max_length=30)
    total = models.CharField(max_length=30)



