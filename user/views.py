from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserSerializer


class UserApi (ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True, )
    def checkEmail(self, request, pk):
        check = False
        if UserModel.objects.filter(cnpj=pk).exists():
            check = True

        return Response({'check': check})
