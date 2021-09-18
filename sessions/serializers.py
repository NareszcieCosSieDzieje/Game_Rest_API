from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'request_id', 'map', 'players', 'number_of_teams']
