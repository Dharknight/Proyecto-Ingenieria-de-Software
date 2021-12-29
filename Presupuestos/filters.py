from apps.Presupuestos.models import Presupuesto
import django_filters
from django_filters import DateFilter, CharFilter

class PresupuestoFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="Fecha", lookup_expr='gte',label='Desde')
    finish_date=DateFilter(field_name="Fecha", lookup_expr='lte',label='Hasta')
    
    class Meta:
        model=Presupuesto
        fields=[
        
        ]
        