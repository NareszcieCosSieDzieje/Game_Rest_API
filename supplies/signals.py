from .models import Supply
from .serializers import SupplySerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Supply, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Supply
    kwargs['model_serializer_class'] = SupplySerializer
    post_save_callback(sender, instance, *args, **kwargs)
