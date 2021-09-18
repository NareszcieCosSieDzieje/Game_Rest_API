from django.db import models
from django.utils.translation import gettext_lazy as _


class Attachment(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    class AttachmentType(models.TextChoices):
        SCOPE = 'S', _('Scope')
        DOUBLE_MAGAZINE = 'DM', _('DoubleMagazine')
        GRENADE_LAUNCHER = 'GL', _('GrenadeLauncher')
        LASER_SCOPE = 'LS', _('LaserScope')

    type = models.CharField(
        max_length=2,
        choices=AttachmentType.choices,
    )

    skin = models.ForeignKey(
        'skins.Skin',
        on_delete=models.SET_NULL,  # SET_DEFAULT ?
        blank=True,
        null=True
        # FIXME
    )

    def __str__(self):
        return f"Attachment[{self.id}]: <type: {self.type}> | <skin_id: {self.skin}>"
