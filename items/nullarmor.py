#!/usr/bin/env python3


from items.basicarmor import BasicArmor


class NullArmor(BasicArmor):

    def __init__(self):
        zero = {
            'name': 'No Armor',
            'family': '',
            'damage_protection': 0,
            'damage_disperse': 0,
            'value': 0,
            'quantity': 0,
            'weight': 0}
        super().__init__(**zero)
