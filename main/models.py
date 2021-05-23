from django.db import models
import datetime
# Товар
# url: /api/v1/products/

# Поля:

# название
# описание
# цена
# дата создания
# дата обновления
# Доступные действия: retrieve, list, create, update, destroy.

# Создавать товары могут только админы. Смотреть могут все пользователи.

# Должна быть возможность фильтровать товары по цене и содержимому из названия / описания.

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