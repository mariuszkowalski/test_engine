#!/usr/bin/env python3


from items.basicweapon import BasicWeapon


class NullWeapon(BasicWeapon):

    def __init__(self):
        zero = {
            'name': 'No Weapon',
            'family': '',
            'hands': 'one',
            'damage': (0, 0),
            'pierce': 0,
            'value': 0,
            'quantity': 0,
            'weight': 0
        }
        super().__init__(**zero)
