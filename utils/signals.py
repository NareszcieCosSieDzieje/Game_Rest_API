from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# from arch_sessions.models import ArchSession

from utils.hash_helpers import get_object_hash

# TODO CALCULATE NEW SLUG?


def update_instance(instance, **kwargs):

    if 'model_class' not in kwargs or 'model_serializer_class' not in kwargs:
        raise Exception  # FIXME

    ModelClass = kwargs['model_class']
    ModelSerializerClass = kwargs['model_serializer_class']
    callback_method = kwargs['callback_method']

    if hasattr(instance, 'request_id'):

        if (callback_method == 'post_save' and hasattr(instance, 'skip_signal_post_save')) \
                or (callback_method == 'm2m_changed' and hasattr(instance, 'skip_signal_m2m_changed')):
            return

        # Create hash for obj
        instance.request_id = get_object_hash(instance, ModelSerializerClass)

        if hasattr(instance, 'revision_id'):
            instance.revision_id += 1  # FIXME PRZEPELNIENIE?

        if callback_method == 'post_save':
            instance.skip_signal_post_save = True

        elif callback_method == 'm2m_changed':
            instance.skip_signal_m2m_changed = True

        instance.save()
    else:
        return


def post_save_callback(sender, instance, *args, **kwargs):
    kwargs['callback_method'] = 'post_save'
    update_instance(instance, **kwargs)


def m2m_changed_callback(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        kwargs['callback_method'] = 'm2m_changed'
        update_instance(instance, **kwargs)
