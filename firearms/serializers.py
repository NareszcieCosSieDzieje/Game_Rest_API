from rest_framework import serializers
from .models import Firearm


class FirearmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firearm # FIXME ADD revision id ?
        fields = ['id', 'request_id', 'name', 'type', 'fire_rate', 'clip_capacity', 'clip_cartridges',
                  'damage', 'ammunition_type', 'attachments'] # 'skin'
