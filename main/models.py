from django.db import models
import datetime

class Product(models.Model):
    """Модель товара интернет магазина."""

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, default="")
    price = models.FloatField()
    creation_date = models.DateField(
        auto_now=True
        )
    update_date = models.DateField(
        default=datetime.date(1970, 1, 1),
        )

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.title