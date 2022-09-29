
# flake8: noqa E722, E501

from church.models import Church
from informations.models import Adress
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Missionary
from .serializers import MissionarySerializer


class MissionaryApi (ModelViewSet):
    queryset = Missionary.objects.all()
    serializer_class = MissionarySerializer

    @action(detail=True, methods=['get'], )
    def getmissionaryData(request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            church = Missionary.objects.get(user=user)
            return Response(MissionarySerializer(church).data, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        post_data = request.data

        adressCheck = post_data["id_adress"]

        if post_data["adress"] is None:
            adress = Adress.objects.get(id=adressCheck)
        else:
            adress = Adress.objects.create(
                adress=post_data["adress"]["adress"],
                zip_code=post_data["adress"]["zip_code"],
                number=post_data["adress"]["number"],
                city=post_data["adress"]["city"],
                uf=post_data["adress"]['uf'],
                district=post_data["adress"]['district']
            )
            adress.save()

        new_user = UserModel.objects.create_superuser(
            post_data['user']['category'],
            post_data['user']['username'],
            True,
            post_data["user"]["email"],
            post_data["user"]["password"]
        )

        church = Church.objects.get(id=post_data['id_church'])

        new_Missionary = Missionary.objects.create(
            user=new_user,
            adress=adress,
            church=church,
            id_church=post_data['id_church'],
            id_adress=post_data['id_adress'],
            fullName=post_data['fullName']
        )

        new_Missionary.save()
        serializer = MissionarySerializer(new_Missionary)

        return Response(serializer.data)
