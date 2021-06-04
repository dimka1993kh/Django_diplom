import datetime

import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.parametrize(
    ["creation_date", "update_date", "expected_status"],
    [
        [datetime.datetime.now().date(), None, HTTP_201_CREATED],
    ]
)
@pytest.mark.django_db
def test_create_Product(admin_client, expected_status, creation_date, update_date):
    url = reverse("product-list")
    if update_date is not None:
        product_payload = {
            "title": "test_product",
            "description": "test_description",
            "price": 999.1,
            "creation_date": creation_date,
            "update_date": update_date,
        }
    else:
        product_payload = {
            "title": "test_product",
            "description": "test_description",
            "price": 999.1,
            "creation_date": creation_date,
        }

    resp = admin_client.post(url, product_payload)
    print(resp.data)
    assert resp.status_code == expected_status

    admin_client.credentials()