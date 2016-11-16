#!/usr/bin/env python3


from basicinventory import BasicInventory
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
        self.inventory = CharacterInventory()

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


class CharacterInventory(BasicInventory):

    def __init__(self):
        super().__init__()
        self.total_weight = 0

    def _calculate_total_weight(self):
        '''
        Calculate total weight of all items in the inventory.
        '''

        if len(self.all) > 0:
            for item in self.all:

                if item.quantity > 1:
                    self.total_weight += item.quantity * item.weight
                elif item.quantity == 1:
                    self.total_weight += item.weight

    def add_to_inventory(self, current_item):
        '''
        Adds current item to the inventory list.

        Args:
            current_item: instance - instance of the valid item class.
        '''

        increased_quantity = False
        if len(self.all) == 0:
            self.all.append(current_item)
            self.total_weight += current_item.weight

        elif len(self.all) >= 1:

            for item in self.all:

                if item.name == current_item.name:
                    item.quantity += 1
                    self.total_weight += current_item.weight
                    increased_quantity = True

            if not increased_quantity:
                self.all.append(current_item)
                self.total_weight += current_item.weight


    def remove_from_inventory(self, current_name):
        '''
        Removes item from the inventory list using name of the item, if there is more items than
        one quantity of given item is decreased.

        Args:
            current_name: str - string name of the item.
        '''

        if len(self.all) > 0:

            for i, item in enumerate(self.all):

                if item.name == current_name:

                    if item.quantity == 1:
                        self.all.pop(i)
                        self.total_weight -= item.weight
                    else:
                        item.quantity -= 1
                        self.total_weight -= item.weight


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
