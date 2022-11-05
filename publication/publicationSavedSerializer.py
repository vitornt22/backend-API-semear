from rest_framework import serializers
from user.models import UserModel
from user.serializers import UserSerializer

from .models import PublicationSaved
from .serializers import PublicationSerializer


class PublicationSavedSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicationSaved
        fields = '__all__'


class PublicationSavedSerializerRead(serializers.ModelSerializer):
    user = UserSerializer()
    publication = PublicationSerializer()

    class Meta:
        model = PublicationSaved
        fields = '__all__'
