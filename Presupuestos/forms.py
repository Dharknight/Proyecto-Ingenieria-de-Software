from typing import OrderedDict
from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from apps.Presupuestos.models import Presupuesto
from apps.Repuestos.models import Repuesto
from apps.Reservas.models import Reserva

class Form_add_presupuesto(forms.ModelForm):
    class Meta:
        model=Presupuesto
        fields=[
        'Reserva',
        'Repuesto',
        'Diagnostico',
        'Fecha',]
        widgets={
        'Reserva':forms.Select(attrs={'class':'form-control'}),
        'Repuesto':forms.Select(attrs={'class':'form-control'}),
        'Diagnostico':forms.TextInput(attrs={'class':'form-control'}),
        'Fecha':forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
class Form_add_presupuesto_reserva(forms.ModelForm):
    class Meta:
        model=Presupuesto
        fields=[
        'Reserva',
        'Repuesto',
        'Diagnostico',
        'Fecha',]
        widgets={
        'Reserva':forms.Select(attrs={'class':'form-control'}),
        'Repuesto':forms.Select(attrs={'class':'form-control'}),
        'Diagnostico':forms.TextInput(attrs={'class':'form-control'}),
        'Fecha':forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }

        
        
        