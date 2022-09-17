from rest_framework import serializers

from .models import PIX, Adress, BankData


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = '__all__'


class BankDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankData
        fields = '__all__'


class PIXSerializer(serializers.ModelSerializer):

    class Meta:
        model = PIX
        fields = '__all__'
