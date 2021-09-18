from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Firearm(models.Model):

    class FirearmType(models.TextChoices):
        HAND_GUN = 'HG', _('HandGun')
        LONG_GUN = 'LG', _('LongGun')

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    name = models.CharField(max_length=20)
    # slug = models.SlugField()

    type = models.CharField(
        max_length=2,
        choices=FirearmType.choices
        # default=CaliberType.MEDIUM_BORE
    )

    fire_rate = models.FloatField(validators=[MinValueValidator(limit_value=0.0, message="Fire rate has to be greter than 0.")])  # per second
    clip_capacity = models.PositiveIntegerField()
    clip_cartridges = models.PositiveIntegerField()
    # clips = models.PositiveIntegerField() # FIXME?

    damage = models.FloatField(default=1.0, validators=[
        MinValueValidator(limit_value=0.0, message="Cannot deal less than 0 damage."),
        MaxValueValidator(limit_value=100.0, message="Cannot deal more than 100 damage.")
    ])

    ammunition_type = models.ForeignKey(
        'ammunition.Ammunition',
        null=True,
        blank=True,
        on_delete=models.SET_NULL, # SET_DEFAULT?? # FIXME JAKIES ON DELETE?
    )

    skin = models.ForeignKey(
        'skins.Skin',
        on_delete=models.SET_NULL,  # SET_DEFAULT ?
        blank=True,
        null=True # TODO: ADD DEFUALT?
        # FIXME
    )

    attachments = models.ManyToManyField(
        'attachments.Attachment',
        blank=True,
        null=True
        # FIXME!
    )
