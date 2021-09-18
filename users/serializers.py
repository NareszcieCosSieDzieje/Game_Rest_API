from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'request_id', 'username', 'ranking', 'score', 'played_matches'] # 'skin'
