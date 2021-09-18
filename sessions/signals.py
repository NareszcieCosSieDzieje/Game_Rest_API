from .models import Session
from .serializers import SessionSerializer

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from utils.signals import post_save_callback, m2m_changed_callback


@receiver(post_save, sender=Session, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Session
    kwargs['model_serializer_class'] = SessionSerializer
    post_save_callback(sender, instance, *args, **kwargs)


@receiver(m2m_changed, sender=Session.players.through, weak=False)
def m2m_changed_wrapper(sender, instance, action, *args, **kwargs):
    kwargs['model_class'] = Session
    kwargs['model_serializer_class'] = SessionSerializer
    m2m_changed_callback(sender, instance, action, *args, **kwargs)
