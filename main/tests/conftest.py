import pytest 
# from model_bakery import baker
from rest_framework.test import APIClient

from main.models import Product


@pytest.fixture
def create_api_client():
    return APIClient()

@pytest.fixture
def create_products_for_test_product_review():
    product_one = Product.objects.create(
        id=1,
        title="test1",
        description="test1",
        price=100.0,
    )
    product_two = Product.objects.create(
        id=2,
        title="test2",
        description="test2",
        price=200.0,
    )
    product_three = Product.objects.create(
        id=3,
        title="test3",
        description="test3",
        price=300.0,
    )

    products = [product_one, product_two, product_three]
    return products
