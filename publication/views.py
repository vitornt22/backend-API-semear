
from project.models import Project
from rest_framework import status
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
            a = Project.objects.get(user=post_data['id_user'])

            new_Publication = Publication.objects.create(
                project=a,
                id_user=post_data['id_user'],
                upload=request.FILES['upload'],
                legend=post_data['legend'],
                is_accountability=False,
            )

            new_Publication.save()
            serializer = PublicationSerializer(new_Publication)
            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except Project.DoesNotExist:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)  # noqa
