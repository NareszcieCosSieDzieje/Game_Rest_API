from django.db import models


class Map(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    # graphic = models.ImageField()graphic = models.
    max_players = models.PositiveIntegerField() # FIXME MAX VAL
