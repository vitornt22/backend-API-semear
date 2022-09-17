

# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Adress, BankData
from .serializers import AdressSerializer, BankDataSerializer


class AdressApi (ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer


class BankDataApi (ModelViewSet):
    queryset = BankData.objects.all()
    serializer_class = BankDataSerializer
