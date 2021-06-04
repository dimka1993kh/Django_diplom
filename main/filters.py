from django_filters import rest_framework as filters
from .models import Product, ProductReview

class ProductFilter(filters.FilterSet): 

    """Класс для определения фильтров для модели Product."""

    title = filters.CharFilter(field_name="title",)
    description = filters.CharFilter(field_name="description",)
    price_from = filters.NumberFilter(field_name="price", lookup_expr="gte",)
    price_to = filters.NumberFilter(field_name="price", lookup_expr="lte",)

    class Meta:
        model = Product
        fields=["title", "description", "price_from", "price_to"]

class ProductReviewFilter(filters.FilterSet): 

    """Класс для определения фильтров для модели ProductReview."""

    ID_user = filters.NumberFilter(field_name="ID_review_author")
    ID_product = filters.NumberFilter(field_name="ID_product")
    create_date = filters.DateFilter(field_name="creation_date")

    class Meta:
        model = ProductReview
        fields=["ID_user", "ID_product", "create_date"]