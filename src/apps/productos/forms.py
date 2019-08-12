from django import forms
from apps.productos.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto


        fields = [
            'nom_producto',
            'pre_venta',
            'pre_compra',
            'fecha_ven',
            'stock',
            'cod_cate',
            'cod_prove',
            'cod_pres',
        ]

        labels = {
            'nom_producto':'Nombre Producto',
            'pre_venta':'Precio Venta',
            'pre_compra':'Precio Compra',
            'fecha_ven':'Fecha Vencimiento',
            'stock':'Stock',
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


