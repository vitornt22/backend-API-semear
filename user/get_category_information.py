from rest_framework import serializers

from church.models import Church
from missionary.models import Missionary
from project.models import Project
from user.models import Information


class InformationSerializer (serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


'''
def get_Data(category, id):
    try:
        if category == 'project':
            projects = Project.objects.get(id=id)
            return ProjectSerializer(projects).data
        if category == 'missionary':
            missionary = Missionary.objects.get(id=id)
            return MissionarySerializer(missionary).data
    except:
        return None
'''


def get_category_information(category, id):
    if category == 'church':
        try:
            church = Church.objects.get(user=id)
            return InformationSerializer(church.information).data
        except Church.DoesNotExist:
            return None
    if category == 'project':
        try:
            project = Project.objects.get(user=id)
            return InformationSerializer(project.information).data
        except Project.DoesNotExist:
            return None
    if category == 'donor':
        return None
    if category == 'missionary':
        try:
            missionary = Missionary.objects.get(user=id)
            return InformationSerializer(missionary.information).data
        except Missionary.DoesNotExist:
            return None
