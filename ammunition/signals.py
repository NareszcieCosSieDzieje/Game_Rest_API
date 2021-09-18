from .models import Ammunition
from .serializers import AmmunitionSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Ammunition, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Ammunition
    kwargs['model_serializer_class'] = AmmunitionSerializer
    post_save_callback(sender, instance, *args, **kwargs)
