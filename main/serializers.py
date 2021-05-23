# TODO: опишите сериализаторы
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import request
import datetime

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
        default=datetime.date(1970, 1, 1)
    )

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной")
        else:
            return value

    def validate_creation_date(self, value):
        if value != datetime.datetime.now().date():
            raise serializers.ValidationError("Дата создания должна быть сегоднешним днем")

    def validate_update_date(self, value):
        if value == datetime.date(1970, 1, 1):
            return value
        elif value != datetime.datetime.now().date():
            raise serializers.ValidationError("Дата обновления должна быть сегоднешним днем") 
        
    
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "creation_date", "update_date"]