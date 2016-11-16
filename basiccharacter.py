#!/usr/bin/env python3


from basicstats import BasicStats
from basicskills import BasicCombatSkills
from items import BasicArmor, BasicWeapon, BasicAmmo, BasicConsumable, BasicMisc, \
    NullArmor, NullWeapon, NullAmmo


class BasicCharacter:
    def __init__(self, name, *args, **kwargs):
        '''
        Creates character with basic attributes.

        Args:
            name: str - name of the character
            max_hp: int - max hp of the character
            max_mp: int - max mp of the character

        Default attributes:
            alive: bool - if the instance is active or not
            current_hp: int - match max hp when created
            current_mp: int - match max mp when created
        '''

        self.stats = BasicStats(**kwargs)
        self.combat_skills = BasicCombatSkills(**kwargs)
        self.equipment = BasicEquipment(**kwargs)
        self.inventory = BasicInventory()

        self.alive = True
        self.name = name
        self.max_hp = self.stats.strength + 2 * self.stats.endurance
        self.max_mp = self.stats.intelligence + 2 * self.stats.wisdom
        self.current_hp = self.max_hp
        self.current_mp = self.max_mp

    def take_hp(self, value):
        '''
        Calculate hp loss.

        Args:
            value: int - hp to loss
        '''
        self.current_hp -= value

        if self.current_hp <= 0:
            self.current_hp = 0
            self.alive = False

    def give_hp(self, value):
        '''
        Calculate hp gain.

        Args:
             value: int - hp to gain
        '''
        self.current_hp += value

        if self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp

    def take_mp(self, value):
        '''
        Calculate mp loss.

        Args:
            value: int - mp to loss
        '''
        self.current_mp -= value

        if self.current_mp <= 0:
            self.current_mp = 0
            self.alive = False

    def give_mp(self, value):
        '''
        Calculate mp gain.

        Args:
            value: int - mp to gain
        '''
        self.current_mp += value

        if self.current_mp >= self.max_mp:
            self.current_mp = self.max_mp

    def show_essentials(self):
        '''
        Shows essential attributes of the class.

        Return:
            str - contains assigned attributes
        '''

        return 'name: {}, hp: {}/{}, mp: {}/{}'.format(
            self.name,
            self.current_hp,
            self.max_hp,
            self.current_mp,
            self.max_mp)


class BasicInventory:

    def __init__(self):
        self.all = {
            'weapons': {
                'sword': [],
                'axe': [],
                'blunt': [],
                'spear': [],
                'throw': [],
                'bow': [],
                'crossbow': []
            },
            'armors': {
                'head': [],
                'torso': [],
                'back': [],
                'arms': [],
                'legs': [],
                'feet': []
            },
            'ammunition':{
                'arrows': [],
                'bolts': []
            },
            'consumable': {
                'food': [],
                'potions': []
            },
            'misc':{
                'books': [],
                'scrolls': []
            }
        }

    def add_to_inventory(self, current_item):
        if isinstance(current_item, BasicWeapon):
            self.all['weapons'][current_item.family].append(current_item)

        elif isinstance(current_item, BasicArmor):
            self.all['armors'][current_item.family].append(current_item)

        elif isinstance(current_item, BasicAmmo):
            self.all['ammunition'][current_item.family].append(current_item)

        elif isinstance(current_item, BasicConsumable):
            self.all['consumable'][current_item.family].append(current_item)

        elif isinstance(current_item, BasicMisc):
            self.all['misc'][current_item.family].append(current_item)


    def remove_from_inventory(self, current_name):
        for k, v in self.all.items():

            for l, b in v.items():

                for i, element in enumerate(b):

                    if element.name == current_name:
                        self.all[k][l].pop(i)

    def show_inventory(self):
        print(self.all)

    def show_inventory_all(self):
        for k, v in self.all.items():
            for l, b in v.items():
                for i, element in enumerate(b):
                    print(element.show_stats())

class BasicEquipment:

    def __init__(self, **kwargs):
        self.head = kwargs.get('head', NullArmor())
        self.torso = kwargs.get('torso', NullArmor())
        self.back = kwargs.get('back', NullArmor())
        self.arms = kwargs.get('arms', NullArmor())
        self.legs = kwargs.get('legs', NullArmor())
        self.feet = kwargs.get('feet', NullArmor())

        self.hand = kwargs.get('hand', NullWeapon())
        self.off_hand = kwargs.get('off_hand', NullArmor())
        self.quiver = kwargs.get('quiver', NullAmmo())
