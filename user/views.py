from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserSerializer


class UserApi (ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
