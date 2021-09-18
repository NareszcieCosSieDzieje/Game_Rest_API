from django.db import models
from django.utils.translation import gettext_lazy as _


class Supply(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    class SupplyType(models.TextChoices):
        HEALTH = 'H', _('Health')
        CURE = 'C', _('Cure')
        ENHANCEMENT = 'E', _('Enhancement')

    duration = models.FloatField() # HOW LONG IT LASTS

    skin = models.ForeignKey(
        'skins.Skin',
        on_delete=models.SET_NULL,  # SET_DEFAULT ?
        blank=True,
        null=True
        # FIXME
    )
