from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from .models import Player
from firearms.models import Firearm
from collections import Counter
# from django.core.validators import *


# def player_weapons_validator(player: Player):
# def player_weapons_validator(player):
#     firearms = player.firearms.all()
#     if firearms:
#         firearm_types_counter = Counter([f.type for f in firearms.all()])
#         if len(list(firearm_types_counter.keys())) > 2 or any(map(lambda x: True if x > 1 else False,
#                                                                   list(firearm_types_counter.values()))):
#             raise ValidationError(
#                 _('A player can only have 2 different firearm types, and no more than one of each type.'
#                   '\nGiven firearms %(firearms)'),
#                 params={'firearms': firearms},
#             )

# def firearms_field_changed(sender, **kwargs):
#     instance = kwargs['instance']
#     firearms = instance.firearms.all()
#     if firearms:
#         firearm_types_counter = Counter([f.type for f in firearms.all()])
#         if len(list(firearm_types_counter.keys())) > 2 or any(map(lambda x: True if x > 1 else False,
#                                                                   list(firearm_types_counter.values()))):
#             raise ValidationError(
#                 _('A player can only have 2 different firearm types, and no more than one of each type.'
#                   '\nGiven firearms %(firearms)'),
#                 params={'firearms': firearms},
#             )

# TODO: WALIDACJA SUPPLIES I THROWABLES ZEBY NIE BYLO ZA DUZO
