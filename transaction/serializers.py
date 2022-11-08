
from rest_framework import serializers

from church.models import Church
from church.serializers import ChurchSerializer
from donor.models import Donor
from donor.serializers import DonorSerializer
from missionary.models import Missionary
from missionary.serializers import MissionarySerializer
from project.models import Project
from project.serializers import ProjectSerializer
from user.serializers import UserSerializer

from .models import Donation


def get_data(category, id):
    if category == 'project':
        try:
            project = Project.objects.get(user=id)
            return ProjectSerializer(project).data
        except Project.DoesNotExist:
            return None
    if category == 'donor':
        try:
            donor = Donor.objects.get(user=id)
            return DonorSerializer(donor).data
        except Donor.DoesNotExist:
            return None
    if category == 'church':
        try:
            project = Church.objects.get(user=id)
            return ChurchSerializer(project).data
        except Church.DoesNotExist:
            return None
    if category == 'missionary':
        try:
            project = Missionary.objects.get(user=id)
            return MissionarySerializer(project).data
        except Missionary.DoesNotExist:
            return None


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    donor = UserSerializer()
    userData = serializers.SerializerMethodField('get_user_data')
    donorData = serializers.SerializerMethodField('get_donor_data')

    class Meta:
        model = Donation
        fields = '__all__'

    def get_donor_data(self, obj):
        try:
            print(obj.donor.category)
            get_data(obj.donor.category, obj.donor.id)
        except:
            return None

    def get_user_data(self, obj):
        try:
            get_data(obj.user.category, obj.user.id)
        except:
            return None
