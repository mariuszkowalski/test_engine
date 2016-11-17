#!/usr/bin/env python3


from items.basicammo import BasicAmmo


class NullAmmo(BasicAmmo):

    def __init__(self):
        zero = {
            'name': 'No Ammo',
            'family': '',
            'damage_bonus': (0, 0),
            'pierce': 0,
            'value': 0,
            'quantity': 0,
            'weight': 0
        }
        super().__init__(**zero)
