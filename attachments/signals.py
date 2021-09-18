from .models import Attachment
from .serializers import AttachmentSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=Attachment, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = Attachment
    kwargs['model_serializer_class'] = AttachmentSerializer
    post_save_callback(sender, instance, *args, **kwargs)
