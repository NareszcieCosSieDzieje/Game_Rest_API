from django.db import models


class ArchSession(models.Model):

    serialized_map = models.TextField() # FIXME
    serialized_players = models.TextField()