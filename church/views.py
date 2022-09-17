

from informations.models import PIX, Adress, BankData
from informations.serializers import (AdressSerializer, BankDataSerializer,
                                      PIXSerializer)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Church
from .serializers import ChurchSerializer


class ChurchApi (ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer

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

        adress = Adress.objects.create(
            adress=post_data["adress.adress"],
            zip_code=post_data["adress.zip_code"],
            number=post_data["adress.number"],
            city=post_data["adress.city"],
            uf=post_data['adress.uf'],
            district=post_data['adress.district']
        )
        adress.save()

        bankData = BankData.objects.create(
            holder=post_data["bankData.holder"],
            cnpj=post_data["bankData.cnpj"],
            bank=post_data["bankData.bank"],
            agency=post_data["bankData.agency"],
            digitAgency=post_data['bankData.digitAgency'],
            account=post_data['bankData.account'],
            digitAccount=post_data['bankData.digitAccount'],
        )
        bankData.save()

        pix = PIX.objects.create(
            typeKey=post_data['pix.typeKey'],
            valueKey=post_data['pix.valueKey']
        )
        pix.save()

        new_church = Church.objects.create(
            user=new_user,
            adress=adress,
            bankData=bankData,
            pix=pix,
            cnpj=post_data['cnpj'],
            ministery=post_data['ministery'],
            name=post_data['name']
        )
        new_church.save()
        serializer = ChurchSerializer(new_church)

        return Response(serializer.data)
