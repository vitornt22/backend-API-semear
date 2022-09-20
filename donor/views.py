

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Donor
from .serializers import DonorSerializer


class DonorApi (ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

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
