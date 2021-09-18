from .models import Map
from .serializers import MapSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Map, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Map
    kwargs['model_serializer_class'] = MapSerializer
    post_save_callback(sender, instance, *args, **kwargs)
