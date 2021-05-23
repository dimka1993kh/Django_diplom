from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet): 

    """Класс для определения фильтров."""
    title = filters.CharFilter(field_name="title",)
    description = filters.CharFilter(field_name="description",)
    price_from = filters.NumberFilter(field_name="price", lookup_expr="gte",)
    price_to = filters.NumberFilter(field_name="price", lookup_expr="lte",)

    class Meta:
        model = Product
        fields=["title", "description", "price_from", "price_to"]