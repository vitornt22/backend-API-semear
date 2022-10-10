from rest_framework import serializers

from .models import PublicationSaved


class PublicationSavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationSaved
        fields = '__all__'
