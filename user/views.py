# flake8: noqa: E501
import publication
from publication.models import Like
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Information, UserModel
from .serializers import InformationSerializer, UserSerializer


class InformationApi (ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = ['AllowAny']


class UserApi (ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['AllowAny']

    @action(methods=['GET'], detail=True)
    def getButtonLike(self, request, pk, *args, **kwargs):
        pub = int(kwargs['target_id'])
        print(pub)
        if Like.objects.filter(user=pk, publication=pub).exists():
            return Response({"label": "Descurtir"})
        else:
            return Response({"label": "Descurtir"})

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class checkEmail(generics.RetrieveAPIView):
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, email, *args, **kwargs):
        print('EMAIL:', email)
        try:
            a = UserModel.objects.filter(email=email).exists()
        except UserModel.DoesNotExist:
            a = False

        return Response({'check': a})


class checkUsername(generics.RetrieveAPIView):
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, username, *args, **kwargs):
        print('EMAIL:', username)
        try:
            a = UserModel.objects.filter(username=username).exists()
        except UserModel.DoesNotExist:
            a = False

        return Response({'check': a})


class getCategory(generics.RetrieveAPIView):
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    queryset = UserModel.objects.all()
    serializer = UserSerializer

    def get(self, request, email, *args, **kwargs):
        print('EMAIL:', email)

        try:
            a = UserModel.objects.get(email=email)
            serializer = UserSerializer(a).data
            print('SERIALIZER')
            return Response({'user': serializer}, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({'user': None}, status=status.HTTP_404_NOT_FOUND)
