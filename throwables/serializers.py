
from rest_framework import serializers
from .models import Throwable


class ThrowableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Throwable
        fields = ['id', 'request_id', 'name', 'weight', 'size', 'throw_range', 'damage'] # 'skin'

