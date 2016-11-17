#!/usr/bin/env python3


from items.basicitem import BasicItem


class BasicConsumable(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'potions')
        self.effect = kwargs.get('effect', ('instant', 100))
