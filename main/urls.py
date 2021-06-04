from rest_framework import routers
from .views import ProductViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet, basename="product")
router.register("product_review", ProductReviewViewSet, basename="product_review")

urlpatterns = router.urls