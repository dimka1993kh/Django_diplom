import datetime

import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from main.models import Product
from main.tests.test_models.test_models import assertModels, create_product


@pytest.mark.parametrize(
    ["test_name", "error", "creation_date", "update_date", "expected_status"],
    [
        ["True work", None, datetime.datetime.now().date(), None, HTTP_201_CREATED],
        ["Invalid creation_date", "Дата создания должна быть сегодняшним днем", datetime.datetime(1999, 4, 4).date(), None, HTTP_400_BAD_REQUEST],
    ]
)
@pytest.mark.django_db
def test_create_Product(admin_client, expected_status, creation_date, update_date, test_name, error):
    url = reverse("product-list")

    product_payload = {
        "id": 1,
        "title": "test_product",
        "description": "test_description",
        "price": 999.1,
        "creation_date": creation_date,
    }

    true_product = Product(
        id=product_payload["id"],
        title=product_payload["title"],
        description=product_payload["description"],
        price=product_payload["price"],
        creation_date=product_payload["creation_date"],
    )

    if update_date is not None:
        product_payload["update_date"] = update_date
        true_product.update_date = update_date

    resp = admin_client.post(url, product_payload)
    assert resp.status_code == expected_status

    products = Product.objects.all()

    if error:
        assert len(products) == 0
        assert list(resp.data.values())[0][0] == error
    else:
        assert len(products) == 1
        assert assertModels(products[0], true_product)

    admin_client.credentials()
