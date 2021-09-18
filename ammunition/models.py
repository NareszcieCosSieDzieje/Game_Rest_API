from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

from utils.hash_helpers import get_object_hash


class Ammunition(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, editable=False)

    LARGE_BORE_THRESHOLD = 0.40
    MEDIUM_BORE_THRESHOLD = 0.33
    SMALL_BORE_THRESHOLD = 0.23
    MINIATURE_BORE_THRESHOLD = 0.0

    class CaliberType(models.TextChoices):
        MINIATURE_BORE = 'MNB', _('MiniatureBore')
        SMALL_BORE = 'SB', _('SmallBore')
        MEDIUM_BORE = 'MB', _('MediumBore')
        LARGE_BORE = 'LB', _('LargeBore')

    caliber = models.DecimalField(max_digits=5, decimal_places=3, db_index=True)  # in inches
    CALIBER_SUFFIX = "inches"

    caliber_type = models.CharField(
        max_length=3,
        choices=CaliberType.choices
        # default=CaliberType.MEDIUM_BORE
    )

    damage_modifier = models.FloatField(default=1.0)  # BASED ON CALIBER TYPE

    skin = models.ForeignKey(
        'skins.Skin',
        on_delete=models.SET_NULL, # SET_DEFAULT ?
        related_name='Ammunition',
        blank=True,
        null=True
        #FIXME
    )

    def set_caliber_type(self):
        if self.caliber >= self.LARGE_BORE_THRESHOLD:
            self.caliber_type = self.CaliberType.LARGE_BORE
        elif self.caliber >= self.MEDIUM_BORE_THRESHOLD:
            self.caliber_type = self.CaliberType.MEDIUM_BORE
        elif self.caliber >= self.SMALL_BORE_THRESHOLD:
            self.caliber_type = self.CaliberType.SMALL_BORE
        else:
            self.caliber_type = self.CaliberType.MINIATURE_BORE

    def set_damage_modifier(self): # TODO: CONVERT TO FLOAT?
        if self.caliber_type == self.CaliberType.LARGE_BORE:
            self.damage_modifier = (self.caliber - Decimal(self.LARGE_BORE_THRESHOLD)) / Decimal(self.LARGE_BORE_THRESHOLD)
        elif self.caliber_type == self.CaliberType.MEDIUM_BORE:
            self.damage_modifier = 1.0
        elif self.caliber_type == self.CaliberType.SMALL_BORE:
            self.damage_modifier = (Decimal(self.MEDIUM_BORE_THRESHOLD) - self.caliber) / Decimal(self.MEDIUM_BORE_THRESHOLD)
        elif self.caliber_type == self.CaliberType.MINIATURE_BORE:
            self.damage_modifier = (Decimal(self.MEDIUM_BORE_THRESHOLD) - self.caliber) / Decimal(self.MEDIUM_BORE_THRESHOLD)
