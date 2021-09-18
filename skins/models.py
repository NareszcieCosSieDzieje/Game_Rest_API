from django.db import models


class Skin(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    name = models.CharField(unique=True, max_length=20)
    slug = models.SlugField()
    # image = models.ImageField()