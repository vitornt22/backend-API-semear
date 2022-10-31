from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserModel

from .models import Donation
from .serializers import TransactionSerializer


# Create your views here.
class TransactionApi(ModelViewSet):
    queryset = Donation.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer

    @action(methods=['GET'], detail=False)
    def getAllTransactions(self, request, *args, **kwargs):
        transactions = Donation.objects.all()
        return Response(TransactionSerializer(transactions, many=True).data, status=status.HTTP_200_OK)  # noqa

    @action(methods=['GET'], detail=True)
    def getTransactionValidations(self, request, pk, *args, **kwargs):
        try:
            donations = Donation.objects.filter(
                user=pk, valid=False).order_by('-created_at')
            return Response(TransactionSerializer(donations, many=True).data, status=status.HTTP_200_OK)  # noqa
        except Donation.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def getDonations(self, request, pk, *args, **kwargs):
        try:
            donations = Donation.objects.filter(
                user=pk, valid=True).order_by('-created_at')
            donations = TransactionSerializer(donations, many=True).data
            send = Donation.objects.filter(donor=pk, valid=True)
            send = TransactionSerializer(send, many=True).data
            return Response({'send': send, 'receive': donations}, status=status.HTTP_200_OK)  # noqa
        except Donation.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def setValidation(self, request, pk, *args, **kwargs):
        try:
            donation = Donation.objects.get(id=pk)
            donation.valid = True
            donation.save()
            return Response(status=status.HTTP_200_OK)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def recuseDonation(self, request, pk, *args, **kwargs):
        try:
            donation = Donation.objects.get(id=pk)
            donation.recused = True
            donation.valid = False
            donation.save()
            return Response(status=status.HTTP_200_OK)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def deleteDonation(self, request, pk, *args, **kwargs):
        try:
            donation = Donation.objects.get(id=pk)
            donation.delete()
            return Response(status=status.HTTP_200_OK)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

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
