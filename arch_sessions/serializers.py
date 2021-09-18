from rest_framework import serializers
from .models import ArchSession


class ArchSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchSession
        fields = ['id', 'serialized_map', 'serialized_players']
