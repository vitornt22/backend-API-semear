

from church.models import Church
from donor.models import Donor
from informations.models import PIX, Adress, BankData
from missionary.models import Missionary
from rest_framework import serializers
from user.models import Information, UserModel

from project.models import Project


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
            church = Church.objects.get(user=id)
            return InformationSerializer(church.information).data
        if category == 'project':
            project = Project.objects.get(user=id)
            return InformationSerializer(project.information).data
        if category == 'donor':
            return None
        if category == 'missionary':
            missionary = Missionary.objects.get(user=id)
            return InformationSerializer(missionary.information).data


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
