from datetime import datetime

from main.models import Product

new_product = Product(
    id=1,
    title="test_product",
    description="test_description",
    price=888.9,
    creation_date=datetime.now().date()
)