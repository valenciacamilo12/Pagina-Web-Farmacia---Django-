from django.db import models



class Empleado(models.Model):
    cod_emp = models.AutoField(primary_key=True, unique=True)
    nom_emp = models.CharField(max_length=30)
    dir_emp = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    celular = models.IntegerField()