from rest_framework import serializers

from .models import BankData


class BankDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankData
        fields = "__all__"
