from .models import Player
from .serializers import PlayerSerializer

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from utils.signals import post_save_callback, m2m_changed_callback


@receiver(post_save, sender=Player, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Player
    kwargs['model_serializer_class'] = PlayerSerializer
    post_save_callback(sender, instance, *args, **kwargs)


@receiver(m2m_changed, weak=False) # FIXME CO Z sender m2m fields -> firearms, throwables, supplies
def m2m_changed_wrapper(sender, instance, action, *args, **kwargs):
    kwargs['model_class'] = Player
    kwargs['model_serializer_class'] = PlayerSerializer
    m2m_changed_callback(sender, instance, action, *args, **kwargs)
