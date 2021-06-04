from django.db import models
import datetime
from .data import choises_for_rating

class Product(models.Model):
    """Модель товара интернет магазина."""

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, default="")
    price = models.FloatField()
    creation_date = models.DateField(
        auto_now=True
        )
    update_date = models.DateField(
        null=True,
        default=None,
        )

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.title

class ProductReview(models.Model):
    """Модель отзыва на товар интернет магазина."""

    ID_review_author = models.ForeignKey("auth.User", on_delete=models.PROTECT, blank=False, null=False, verbose_name='Автор отзыва')
    ID_product = models.ForeignKey("Product", on_delete=models.PROTECT, blank=False, null=False, verbose_name='Товар')
    text = models.TextField(max_length=300, default="")
    rating = models.IntegerField(choices=choises_for_rating)
    creation_date = models.DateField(
        auto_now=True
        )
    update_date = models.DateField(
        default=None,
        null=True,
        )

    class Meta:
        db_table = 'product_review'
        verbose_name = 'Отзыв на товар'
        verbose_name_plural = 'Отзывы на товары'
    
    def __str__(self):
        return f"Отзыв пользователя {self.ID_review_author.username} на товар {self.ID_product.title}"
