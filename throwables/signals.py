from .models import Throwable
from .serializers import ThrowableSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Throwable, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Throwable
    kwargs['model_serializer_class'] = ThrowableSerializer
    post_save_callback(sender, instance, *args, **kwargs)
