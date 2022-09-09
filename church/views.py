# flake8: noqa: F401
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ChurchSerializer

# Create your views here.


class ChurchViewSet(ModelViewSet):
    serializer_class = ChurchSerializer
