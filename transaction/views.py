from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Donation
from .serializers import TransactionSerializer


# Create your views here.
class TransactionApi(ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = TransactionSerializer
