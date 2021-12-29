from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from apps.Boletas.models import Boleta

class Form_add_Boleta(forms.ModelForm):
    class Meta:
        model=Boleta
        fields=[
        'Presupuesto']
        widgets={
        'Presupuesto':forms.Select(attrs={'class':'form-control'}),
        }