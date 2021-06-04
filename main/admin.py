from django.contrib import admin
from main.models import Product, ProductReview

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    pass

