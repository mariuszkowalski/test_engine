#!/usr/bin/env python3


from items.nullarmor import NullArmor
from items.nullweapon import NullWeapon
from items.nullammo import NullAmmo


class BasicEquipment:

    def __init__(self, **kwargs):
        '''
        Creates equipment with the currently used items, if the item is not passed in the initialization
        the NullPiece is used instead.
        '''

        self.head = kwargs.get('head', NullArmor())
        self.torso = kwargs.get('torso', NullArmor())
        self.back = kwargs.get('back', NullArmor())
        self.arms = kwargs.get('arms', NullArmor())
        self.legs = kwargs.get('legs', NullArmor())
        self.feet = kwargs.get('feet', NullArmor())

        self.hand = kwargs.get('hand', NullWeapon())
        self.off_hand = kwargs.get('off_hand', NullArmor())
        self.quiver = kwargs.get('quiver', NullAmmo())

        # This is current item when moving back to inventory.
        self.switch_buffer = []

        self._calculate_protection_values()

    def _calculate_protection_values(self):
        self.total_damage_protection = self.head.damage_protection +\
            self.torso.damage_protection +\
            self.back.damage_protection +\
            self.arms.damage_protection +\
            self.legs.damage_protection +\
            self.feet.damage_protection +\
            self.off_hand.damage_protection

        self.total_damage_disperse = self.head.damage_disperse +\
            self.torso.damage_disperse +\
            self.back.damage_disperse +\
            self.arms.damage_disperse +\
            self.legs.damage_disperse +\
            self.feet.damage_disperse +\
            self.off_hand.damage_disperse

    def add_armor_piece(self, current_item):
        if current_item.family == 'head':
            self.switch_buffer.append(self.head)
            self.head = current_item

        elif current_item.family == 'torso':
            self.switch_buffer.append(self.torso)
            self.torso = current_item

        elif current_item.family == 'back':
            self.switch_buffer.append(self.back)
            self.back = current_item

        elif current_item.family == 'arms':
            self.switch_buffer.append(self.arms)
            self.arms = current_item

        elif current_item.family == 'legs':
            self.switch_buffer.append(self.legs)
            self.legs = current_item

        elif current_item.family == 'feet':
            self.switch_buffer.append(self.feet)
            self.feet = current_item

        elif current_item.family == 'off_hand':
            self.switch_buffer.append(self.off_hand)
            self.off_hand = current_item

        self._calculate_protection_values()

    def remove_armor_piece(self, item_name):
        if self.head.name == item_name:
            self.switch_buffer.append(self.head)
            self.head = NullArmor()

        elif self.torso.name == item_name:
            self.switch_buffer.append(self.torso)
            self.torso = NullArmor()

        elif self.back.name == item_name:
            self.switch_buffer.append(self.back)
            self.back = NullArmor()

        elif self.arms.name == item_name:
            self.switch_buffer.append(self.arms)
            self.arms = NullArmor()

        elif self.legs.name == item_name:
            self.switch_buffer.append(self.legs)
            self.legs = NullArmor()

        elif self.feet.name == item_name:
            self.switch_buffer.append(self.feet)
            self.feet = NullArmor()

        elif self.off_hand.name == item_name:
            self.switch_buffer.append(self.off_hand)
            self.off_hand = NullArmor()

        self._calculate_protection_values()
