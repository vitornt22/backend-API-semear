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
        post_data = request.data
        print("REQUEST PUBLICATION", request.data)

        try:
            a = UserModel.objects.get(id=post_data['id'])
        except UserModel.DoesNotExist:
            a = UserModel.objects.get(id=1)

        new_Publication = Publication.objects.create(
            user=a,
            upload=request.FILES['upload'],
            legend=post_data['legend'],
            is_accountability=False
        )

        new_Publication.save()
        serializer = PublicationSerializer(new_Publication)

        return Response(serializer.data)
