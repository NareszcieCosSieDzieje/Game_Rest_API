from django.db import models


class User(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    # avatar = models.ImageField()

    username = models.TextField()
    hashed_password = models.TextField()

    ranking = models.IntegerField()
    score = models.FloatField()
    played_matches = models.IntegerField()
