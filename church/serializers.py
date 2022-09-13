from rest_framework import serializers

from .models import Church


class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = "__all__"
