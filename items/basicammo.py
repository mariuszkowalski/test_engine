#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicAmmo(BasicItem):

    def __init__(self, **kwargs):
        '''
        Class to create ammo items for the bows, crossbows, and throw.

        Args:
            name: str - name of the ammo.
                default value: ''.
            family: str - describes the name of the family, indicator where the ammo is used.
                Viable options = ['arrow', 'bolt', 'rock']
                default value: 'arrow'.
            damage_bonus: touple (int [min_damage], int [max_damage]) - damage bonus to the given weapon.
                default value: (1, 2)
            pierce: int - ability to negate enemy armor damage protection value.
                default value: 0
            value: int - value of the one item piece.
                default value: 0
            quantity: int - describes current quantity in hold of given item.
                default value: 0
            weight: int - weight of the item.
                default value: 0
        '''

        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'arrow')
        self.damage_bonus = kwargs.get('damage_bonus', (1, 2))
        self.pierce = kwargs.get('pierce', 0)
