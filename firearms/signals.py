from .models import Firearm
from .serializers import FirearmSerializer

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from utils.signals import post_save_callback, m2m_changed_callback


@receiver(post_save, sender=Firearm, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Firearm
    kwargs['model_serializer_class'] = FirearmSerializer
    post_save_callback(sender, instance, *args, **kwargs)


@receiver(m2m_changed, sender=Firearm.attachments.through, weak=False)
def m2m_changed_wrapper(sender, instance, action, *args, **kwargs):
    kwargs['model_class'] = Firearm
    kwargs['model_serializer_class'] = FirearmSerializer
    m2m_changed_callback(sender, instance, action, *args, **kwargs)