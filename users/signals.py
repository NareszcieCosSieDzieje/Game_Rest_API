from .models import User
from .serializers import UserSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.signals import post_save_callback


@receiver(post_save, sender=User, weak=False)
def post_save_wrapper(sender, instance, *args, **kwargs):
    kwargs['model_class'] = User
    kwargs['model_serializer_class'] = UserSerializer
    post_save_callback(sender, instance, *args, **kwargs)
