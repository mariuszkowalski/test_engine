#!/usr/bin/env python3


from basicequipment import BasicEquipment
from characterinventory import CharacterInventory
from basicstats import BasicStats
from basiccombatskills import BasicCombatSkills


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
