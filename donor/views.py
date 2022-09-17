

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
            post_data["user.category"],
            post_data["user.username"],
            True if post_data['user.can_post'] == "true" else False,
            post_data["user.email"],
            post_data["user.password"]
        )
        new_user.save()
        new_church = Donor.objects.create(
            user=new_user,
            fullname=post_data['name']
        )
        new_church.save()
        serializer = DonorSerializer(new_church)

        return Response(serializer.data)
