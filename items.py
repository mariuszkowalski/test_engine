#!/usr/bin/env python3


class BasicItem:

    def __init__(self, name='', value=0, quantity=0, weight=0, **kwargs):
        self.name = name
        self.value = value
        self.quantity = quantity
        self.weight = weight


class BasicArmor(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'torso')
        self.damage_protection = kwargs.get('damage_protection', 10)
        self.damage_disperse = kwargs.get('damage_disperse', 10)


class BasicWeapon(BasicItem):

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'sword')
        self.damage = kwargs.get('damage', (1, 10))
        self.pierce = kwargs.get('pierce', 5)

    def show_stats(self):
        return vars(self)


class BasicAmmo(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'arrow')
        self.damage_bonus = kwargs.get('damage_bonus', (1, 2))
        self.pierce = kwargs.get('pierce', 0)


class BasicConsumable(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'potions')
        self.effect = kwargs.get('effect', ('instant', 100))


class BasicMisc(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'books')
        self.effect = kwargs.get('effect', ('permanent', 1))


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


class NullWeapon(BasicWeapon):

    def __init__(self):
        zero = {
            'name': 'No Weapon',
            'family': '',
            'damage': (0, 0),
            'pierce': 0,
            'value': 0,
            'quantity': 0,
            'weight': 0
        }
        super().__init__(**zero)


class NullAmmo(BasicAmmo):

    def __init__(self):
        zero = {
            'name': 'No Ammo',
            'family': '',
            'damage_bonus': (0, 0),
            'pierce': 0,
            'value': 0,
            'quantity': 0,
            'weight': 0
        }
        super().__init__(**zero)
