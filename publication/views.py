from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Publication
from .serializers import PublicationSerializer

# Create your views here.


class PublicationApi (ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def create(self, request, *args, **kwargs):

        return Response({})
