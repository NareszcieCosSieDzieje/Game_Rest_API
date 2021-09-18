from django.db import models
# from django.db.models.signals import m2m_changed
# from django.core.exceptions import ValidationError
# from .validators import player_weapons_validator


class Player(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    user = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT # FIXME
    )

    score = models.FloatField() # FIXME CZY TO MA SENS to raczej w arch sessions czy cos
    team_id = models.IntegerField(db_index=True)

    # ADD DIFFERENT INVENTORY SIZES AND WEIGHTS
    inventory_size = models.IntegerField(default=10)
    inventory_weight = models.FloatField()

    # clip_capacity = models.IntegerField() # FIXME RACZEJ NIECH MAJA WAGE KLIPY??

    # 1 long #1 short
    firearms = models.ManyToManyField( # JAKIS VALIDATOR ZE MOZE MIEC TYLKO 2 BRONKI PO 2 TYPACHs
        'firearms.Firearm',
        # on_delete=models.SET_NULL,
        blank=True,
        null=True,
        # validators=[player_weapons_validator]
    )

    throwables = models.ManyToManyField(
        'throwables.Throwable',
        blank=True,
        null=True
    )

    supplies = models.ManyToManyField(
        'supplies.Supply',
        # on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def increase_score(self, other_player):
        if self.team_id != other_player.team:
            self.score += 100

