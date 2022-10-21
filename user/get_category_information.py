from church.models import Church
from donor.models import Donor
from missionary.models import Missionary
from project.models import Project
from rest_framework import serializers

from user.models import Information


class InformationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


def get_category_information(category, id):
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
