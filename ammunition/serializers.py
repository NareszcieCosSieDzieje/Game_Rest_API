from rest_framework import serializers
from .models import Ammunition


class AmmunitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammunition
        fields = ['id', 'request_id', 'caliber', 'caliber_type'] # 'skin'
