from apps.Boletas.models import Boleta
import django_filters
from django_filters import CharFilter


class BoletaFilter(django_filters.FilterSet):
    class Meta:
        model=Boleta
        fields='__all__'
        