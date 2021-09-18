from .models import Skin
from .serializers import SkinSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Skin, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Skin
    kwargs['model_serializer_class'] = SkinSerializer
    post_save_callback(sender, instance, *args, **kwargs)
