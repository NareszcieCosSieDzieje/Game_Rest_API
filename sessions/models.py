from django.db import models


class Session(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    map = models.ForeignKey(
        'maps.Map',
        on_delete=models.PROTECT
    )

    players = models.ManyToManyField(
        'players.Player',
        blank=True,
        null=True
    )

    number_of_teams = models.PositiveIntegerField() # NUMBER OF DIFFERENT TEAMS

