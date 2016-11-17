#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicArmor(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'torso')
        self.damage_protection = kwargs.get('damage_protection', 10)
        self.damage_disperse = kwargs.get('damage_disperse', 10)
