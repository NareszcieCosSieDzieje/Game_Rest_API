from django.db import models
from django.utils.translation import gettext_lazy as _


class Throwable(models.Model):

    revision_id = models.PositiveIntegerField(default=0, editable=False)
    request_id = models.CharField(max_length=100, default="", editable=False)

    name = models.CharField(max_length=20)
    slug = models.SlugField()

    # JAKAS NADRZEDAN KLASA DO ODZIEDZICZENIA TEGO?
    weight = models.FloatField() # ILE WAZY
    size = models.IntegerField() # ILE MIEJSCA ZAJMUJ | POLA W PLECAKU

    throw_range = models.IntegerField()
    # damage_field = models. # FIXME JAK OPSIAC POLE RAZENIA
    damage = models.FloatField()

    skin = models.ForeignKey(
            'skins.Skin',
            on_delete=models.SET_NULL,  # SET_DEFAULT ?
            blank=True,
            null=True
            # FIXME
    )
