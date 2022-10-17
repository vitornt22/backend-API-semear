
from church.models import Church
from donor.models import Donor
from informations.models import PIX, Adress, BankData
from missionary.models import Missionary
from rest_framework import serializers
from user.models import Information, UserModel

from project.models import Project


class PixSerializer(serializers.ModelSerializer):
    class Meta:
        model = PIX
        fields = '__all__'


class BankDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankData
        fields = '__all__'


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class ChurchSerializer(serializers.ModelSerializer):
    adress = AdressSerializer()
    bankData = BankDataSerializer()
    information = InformationSerializer()
    pix = PixSerializer()

    class Meta:
        model = Church
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    church = ChurchSerializer()
    adress = AdressSerializer()
    information = InformationSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'


class MissionarySerializer(serializers.ModelSerializer):
    church = ChurchSerializer()
    adress = AdressSerializer()
    information = InformationSerializer()

    class Meta:
        model = Missionary
        fields = '__all__'
