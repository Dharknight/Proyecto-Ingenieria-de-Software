from apps.Facturas.models import Factura
import django_filters
from django_filters import CharFilter


class FacturaFilter(django_filters.FilterSet):
    class Meta:
        model=Factura
        fields='__all__'
        