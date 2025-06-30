from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    model = User
    queryset = User.objects.all()

    def get_serializer_class(self):

        return UserSerializer

    def get_permissions(self):

        if self.action in ("update", "partial_update", "destroy"):
            permission_classes = [IsAuthenticated, IsUser]
        elif self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
