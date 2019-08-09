from django.db import models

class Cliente(models.Model):
    cod_cli = models.AutoField(primary_key=True,unique=True)
    nombre_cli = models.CharField(max_length=30)
    dir_cli = models.CharField(max_length=30)
    cod_dis = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    ruc = models.CharField(max_length=30)
    telefono = models.IntegerField()
    celular = models.IntegerField()