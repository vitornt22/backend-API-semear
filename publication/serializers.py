from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Publication
        fields = '__all__'
