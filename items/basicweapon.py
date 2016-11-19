#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicWeapon(BasicItem):

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'sword')
        self.hands = kwargs.get('hands', 'one')
        self.damage = kwargs.get('damage', (1, 10))
        self.pierce = kwargs.get('pierce', 5)

    def show_stats(self):
        return vars(self)
