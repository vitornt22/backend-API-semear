# flake8: noqa E722, E501
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Donor
from .serializers import DonorSerializer


class DonorApi (ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

    @action(detail=True, methods=['get'], )
    def getdonorData(self, request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            donor = Donor.objects.get(user=user)

            if donor is not None:
                return Response(DonorSerializer(donor).data, status=status.HTTP_200_OK)
            else:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_user = UserModel.objects.create_superuser(
            post_data["user"]["category"],
            post_data["user"]["username"],
            False,
            post_data["user"]["email"],
            post_data["user"]["password"]
        )
        new_user.save()
        new_donor = Donor.objects.create(
            user=new_user,
            fullName=post_data['fullName']
        )
        new_donor.save()

        serializer = DonorSerializer(new_donor)

        return Response(serializer.data)
