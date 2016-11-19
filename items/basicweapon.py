#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicWeapon(BasicItem):

    def __init__(self,  **kwargs):
        '''
        Class to create weapon.

        Args:
            name: str - name of the weapon.
                default value: ''.
            family: str - describes the name of the family, indicator where the ammo is used.
                Viable options = ['sword', 'axe', 'blunt', 'spear', 'throw', 'bow', 'crossbow']
                default value: 'sword'.
            hands: str - indicates of the weapon is used with one hand or two hands.
                Viable options = ['one', 'two']
            damage: touple (int [min_damage], int [max_damage]) - damage of the given weapon.
                default value: (1, 10)
            pierce: int - ability to negate enemy armor damage protection value.
                default value: 5
            value: int - value of the one item piece.
                default value: 0
            quantity: int - describes current quantity in hold of given item.
                default value: 0
            weight: int - weight of the item.
                default value: 0
        '''

        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'sword')
        self.hands = kwargs.get('hands', 'one')
        self.damage = kwargs.get('damage', (1, 10))
        self.pierce = kwargs.get('pierce', 5)

    def show_stats(self):
        return vars(self)
