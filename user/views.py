# flake8: noqa: E501
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserSerializer


class UserApi (ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

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
