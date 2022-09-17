from rest_framework.viewsets import ModelViewSet

from .models import Church
from .serializers import ChurchSerializer


class ChurchApi (ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
