import pytest
import datetime

from django.contrib.auth.models import User
from main.models import Product, ProductReview
from main.tests.test_data import new_product


def create_user(username, password):
    return User.objects.create_user(username=username, password=password)

def create_product(model_product):
    return Product.objects.create(
        id=model_product.id,
        title=model_product.title,
        description=model_product.description,
        price=model_product.price,
        creation_date=model_product.creation_date
    )

def create_product_review(model_product_review):
    return ProductReview.objects.create(
        id=model_product_review.id,
        ID_review_author=model_product_review.ID_review_author,
        ID_product=model_product_review.ID_product,
        text=model_product_review.text,
        rating=model_product_review.rating,
    )

def assertModels(obj1, obj2):
    assert obj1.__eq__(obj2)
    # Сравниваем все поля модели
    return list(obj1.__dict__.items())[1::] == list(obj2.__dict__.items())[1::]

@pytest.mark.django_db
def test_create_model_Product():
    products = Product.objects.all()
    assert len(products) == 0

    create_product(new_product)

    products = Product.objects.all()

    assert len(products) == 1
    assert assertModels(products[0], new_product)

@pytest.mark.django_db
def test_create_model_ProductReview():
    products_review = ProductReview.objects.all()
    assert len(products_review) == 0

    user = create_user("testUser", "testPassword12345")
    product = create_product(new_product)

    new_product_review = ProductReview(
        id=1,
        ID_review_author=user,
        ID_product=product,
        text="test_text",
        rating=1,
        creation_date=datetime.datetime.now().date(),
        update_date=None,
    )

    create_product_review(new_product_review)

    products_review = ProductReview.objects.all()
    assert len(products_review) == 1
    assert assertModels(products_review[0], new_product_review)


