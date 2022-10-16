
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Donation
from .serializers import TransactionSerializer


# Create your views here.
class TransactionApi(ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        post_data = request.data
        print("REQUEST PUBLICATION", request.data)

        try:
            user = UserModel.objects.get(id=post_data['user'])
            donor = UserModel.objects.get(id=post_data['donor'])

            new_donation = Donation.objects.create(
                user=user,
                donor=donor,
                value=post_data['value'],
                is_anonymous=bool(post_data['is_anonymous']),
                payment_form=post_data['payment_form'],
                valid=False,
                voucher=request.FILES['voucher'],
            )

            new_donation.save()
            serializer = TransactionSerializer(new_donation)
            return Response(serializer.data, status=status.HTTP_200_OK
                            )
        except UserModel.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)  # noqa
