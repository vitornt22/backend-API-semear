from rest_framework import serializers
from user.models import UserModel
from user.serializers import UserSerializer

from .models import PublicationSaved
from .serializers import PublicationSerializer


class PublicationSavedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    publication = PublicationSerializer(read_only=True)

    class Meta:
        model = PublicationSaved
        fields = '__all__'
