#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicAmmo(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'arrow')
        self.damage_bonus = kwargs.get('damage_bonus', (1, 2))
        self.pierce = kwargs.get('pierce', 0)
