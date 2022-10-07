
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Notification
        fields = '__all__'
