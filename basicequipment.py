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