from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from .filters import ProductFilter

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