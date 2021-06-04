import pytest
import datetime
from rest_framework import status as st
# from main.models import Product
from rest_framework.reverse import reverse

@pytest.mark.parametrize(
    ["text", "rating", "price", "ID_product", "ID_review_author", "creation_date", "update_date", "status"],
    [  
        ["TestOne", 1, 144.9, 1, 1,  datetime.datetime(2000, 2, 2, 2, 2, 2, 2).date(), datetime.datetime(3000, 2, 2, 2, 2, 2, 2).date(),  st.HTTP_201_CREATED],
        ["TestOne", 2, 166.9, 2, 1, datetime.datetime(2080, 2, 2, 2, 2, 2, 2).date(), datetime.datetime(3090, 2, 2, 2, 2, 2, 2).date(),  st.HTTP_201_CREATED],
        ["TestOne", 3, 144.8, 3, 1, datetime.datetime(2500, 2, 2, 2, 2, 2, 2).date(), datetime.datetime(9000, 2, 2, 2, 2, 2, 2).date(),  st.HTTP_201_CREATED],
    ],
    )
@pytest.mark.django_db
def test_create_product_review(create_api_client, create_products_for_test_product_review, text, rating, price, ID_product, ID_review_author, creation_date,  update_date, status):
    client = create_api_client
    url = reverse("product_review-list")
    product_payload = {
        "text": text,
        "rating": rating,
        "price": price,
        "ID_product": ID_product,
        "ID_review_author": ID_review_author,
        "creation_date": creation_date,
        "update_date": update_date,
    }
    resp = client.post(url, product_payload)
    assert resp.status_code == status
