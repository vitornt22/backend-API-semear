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
        if church.information is not None:
            return InformationSerializer(church.information).data
        return None
    if category == 'project':
        project = Project.objects.get(user=id)
        if project.information is not None:
            return InformationSerializer(project.information).data
        return None
    if category == 'donor':
        return None
    if category == 'missionary':
        missionary = Missionary.objects.get(user=id)
        if missionary.information is not None:
            return InformationSerializer(missionary.information).data
        return None
