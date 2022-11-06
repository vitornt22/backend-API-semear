

from rest_framework import serializers

import informations
from church.models import Church
from donor.models import Donor
from informations.models import PIX, Adress, BankData
from missionary.models import Missionary
from project.models import Project
from user.models import Information, UserModel


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    information = serializers.SerializerMethodField('get_category_information')

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email',
                  'category', 'can_post', 'password', 'information')

    def get_category_information(self, obj):
        category = obj.category
        id = obj.id
        if category == 'church':
            try:
                church = Church.objects.get(user=id)
                if church.information is not None:
                    return InformationSerializer(church.information).data
                return None
            except Church.DoesNotExist:
                return None
        if category == 'project':
            try:
                project = Project.objects.get(user=id)
                if project.information is not None:
                    return InformationSerializer(project.information).data
                return None
            except Project.DoesNotExist:
                return None
        if category == 'donor':
            return None
        if category == 'missionary':
            try:
                missionary = Missionary.objects.get(user=id)
                if missionary.information is not None:
                    return InformationSerializer(missionary.information).data
                return None
            except Missionary.DoesNotExist:
                return None


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
        model = Adress
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class ChurchSerializer(serializers.ModelSerializer):
    adress = AdressSerializer()
    user = UserSerializer()
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
