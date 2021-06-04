# TODO: опишите сериализаторы
from rest_framework import serializers, request
from .models import Product, ProductReview
from django.contrib.auth.models import User
from django.contrib import auth
# from django.http import request
import datetime
from .data import choises_for_rating

import inspect

class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели товара."""

    title = serializers.CharField(
        allow_blank=True,
        max_length=50,
        min_length=1,
    )
    description = serializers.CharField(
        allow_blank=True,
        max_length=300,
        min_length=1,
    )
    price = serializers.FloatField(
        min_value=0,
    )
    creation_date = serializers.DateField(
        default=datetime.datetime.now().date(),
    )
    update_date = serializers.DateField(
        default=None
    )

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной")
        else:
            return value

    def validate_creation_date(self, value):
        if value != datetime.datetime.now().date():
            raise serializers.ValidationError("Дата создания должна быть сегодняшним днем")
        else:
            return value

    def validate_update_date(self, value):
        if value is None:
            return value
        elif value != datetime.datetime.now().date():
            raise serializers.ValidationError("Дата обновления должна быть сегоднешним днем") 
        else:
            return value
        
    
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "creation_date", "update_date"]

class ProductReviewSerializer(serializers.ModelSerializer):
    """Сериализатор модели отзыва на товар."""

    ID_review_author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    ID_product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )
    text = serializers.CharField(
        allow_blank=True,
        max_length=300,
        min_length=0,
    )
    rating = serializers.ChoiceField(
        choices=choises_for_rating
    )
    creation_date = serializers.DateField(
        default=datetime.datetime.now().date(),
    )
    update_date = serializers.DateField(
        default=None
    )

    def validate_creation_date(self, value):
        if value != datetime.datetime.now().date():
            raise serializers.ValidationError("Дата создания должна быть сегодняшним днем")
        else:
            return value

    def validate_update_date(self, value):
        if self.context["request"].method in ["PUT", "PATCH"]:
            if value == datetime.datetime.now().date():
                return value
            else:
                raise serializers.ValidationError("Дата обновления должна быть сегоднешним днем") 
        else:
            if value == None:
                return value
        
    class Meta:
        model = ProductReview
        fields = ["id", "ID_review_author", "ID_product", "text", "rating", "creation_date", "update_date"]