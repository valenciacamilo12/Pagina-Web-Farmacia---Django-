from django import forms
from apps.productos.models import Producto
from apps.productos.models import Categoria
from apps.productos.models import Presentacion
from apps.productos.models import Distrito
from apps.productos.models import Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto


        fields = [
            'nom_producto',
            'pre_venta',
            'pre_compra',
            'fecha_ven',
            'stock',
            'producto_imagen',
            'cod_cate',
            'cod_prove',
            'cod_pres',
        ]

        labels = {
            'nom_producto':'Nombre Producto',
            'pre_venta':'Precio Venta',
            'pre_compra':'Precio Compra',
            'fecha_ven':'Feha Venta',
            'stock':'Stock',
            'producto_imagen':'Imagen Producto',
            'cod_cate':'Codigo Categoria',
            'cod_prove':'Codigo Proveedor',
            'cod_pres':'Codigo Presentacion',
        }

        widgets = {
            'nom_producto': forms.TextInput(attrs={'class':'form-control'}),
            'pre_venta': forms.TextInput(attrs={'class':'form-control'}),
            'pre_compra': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ven': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),
            'cod_cate': forms.Select(attrs={'class':'form-control'}),
            'cod_prove': forms.Select(attrs={'class':'form-control'}),
            'cod_pres': forms.Select(attrs={'class':'form-control'}),
        }



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            'nom_cate',
        ]

        labels = {
            'nom_cate': 'Nombre de la Categoria',
        }

        fields = {
            'nom_cate': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion

        fields = [
            'nom_pre',
        ]

        labels = {
            'nom_pre':'Nombre de la Presentacion',
        }

        widgets = {
            'nom_pre': forms.TextInput(attrs={'class':'form-control'}),
        }

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito

        fields = [
            'nom_dis',
            'empleado',

        ]

        labels = {
            'nom_dis':'Nombre Distrito',
            'empleado':'Empleado',
        }

        widgets = {
            'nom_dis':forms.TextInput(attrs={'class':'form-control'}),
            'empleado':forms.Select(attrs={'class':'form-control'}),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor


        fields = [
            'nom_prov',
            'celular',
            'id_distrito',
            'dr_prov',
        ]

        labels = {
            'nom_prov': 'Nombre Proveedor',
            'celular': 'Celular',
            'id_distrito': 'Distrito',
            'dr_prov': 'Direccion Proveedor',
        }

        widgets = {
            'nom_prov': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'id_distrito': forms.TextInput(attrs={'class':'form-control'}),
            'dr_prov': forms.Select(attrs={'class':'form-control'}),
        }