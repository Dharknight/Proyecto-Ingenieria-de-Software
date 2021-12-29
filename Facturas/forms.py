from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from apps.Facturas.models import Factura

class Form_add_Factura(forms.ModelForm):
    class Meta:
        model=Factura
        fields=[
        'Presupuesto']
        widgets={
        'Presupuesto':forms.Select(attrs={'class':'form-control'}),
        }