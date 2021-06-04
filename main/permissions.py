from rest_framework.permissions import BasePermission

class LeaveOnlyOneReview(BasePermission):
    """
    Пользователь может оставить только 1 отзыв на 1 товар.
    """

    message = "Пользователь может оставить только 1 отзыв к 1 товару."

    def has_permission(self, request, view):
        if request.data:
            if not view.queryset.filter(ID_review_author=request.user, ID_product=request.data["ID_product"],):
                return True
        else:
            return True

class OwnReview(BasePermission):
    """
    Пользователь может обновлять и удалять только собственный отзыв.
    """

    message = "Пользователь может обновлять и удалять только собственный отзыв"

    
    def has_permission(self, request, view):
        id_object_being_updated = view.kwargs.get('pk')
        if request.user.is_staff or view.queryset.get(id=id_object_being_updated).ID_review_author == request.user:
            return True