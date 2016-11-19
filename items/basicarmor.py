#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicArmor(BasicItem):

    def __init__(self, **kwargs):
        '''
        Class to create armors for the different parts of the body.

        Args:
            name: str - name of the armor.
                default value: ''.
            family: str - describes the name of the family, indicator where the armor is wear.
                Viable options = ['head', 'torso', 'back', 'arms', 'legs', 'feet', 'off_hand']
                default value: 'torso'.
            damage_protection: int - how many damage points is absorbed by the armor.
                default value: 10
            damage_disperse: int - how many percent of the damage is dispersed by the inner layers of
                the armor after the armor is penetrated.
                default value: 10
            value: int - value of the one item piece.
                default value: 0
            quantity: int - describes current quantity in hold of given item.
                default value: 0
            weight: int - weight of the item.
                default value: 0
        '''

        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'torso')
        self.damage_protection = kwargs.get('damage_protection', 10)
        self.damage_disperse = kwargs.get('damage_disperse', 10)
