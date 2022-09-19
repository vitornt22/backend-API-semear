from cgitb import lookup
from codecs import lookup_error

from rest_framework import generics
from rest_framework.decorators import action
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
