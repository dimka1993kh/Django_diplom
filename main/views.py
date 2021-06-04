from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer
from rest_framework import permissions, status
from .permissions import LeaveOnlyOneReview, OwnReview
from rest_framework.response import Response
from .filters import ProductFilter, ProductReviewFilter

class ProductViewSet(ModelViewSet):
    """ViewSet для продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        """Проверка пользователя. Для просмотра продуктов пользователь 
        должен быть IsAuthenticated, для создания продуктов IsAuthenticated и IsAdminUser."""
        
        if self.action == 'list':
            permission = [permissions.IsAuthenticated]
        else:
            permission = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return [permission() for permission in permission]

class  ProductReviewViewSet(ModelViewSet):
    """ViewSet для продукта."""

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filterset_class = ProductReviewFilter

    def get_permissions(self):
        """Проверка пользователя. Для просмотра продуктов пользователь 
        должен быть IsAuthenticated, для создания продуктов IsAuthenticated и IsAdminUser."""
        
        permissions_list = []

        if self.action != "list":
            permissions_list = [permissions.IsAuthenticated, ]
        
        if self.action == "create":
            permissions_list = [LeaveOnlyOneReview, ]

        if self.action in ["update", "destroy"]:
            permissions_list = [OwnReview, ]

        return [permission() for permission in permissions_list]