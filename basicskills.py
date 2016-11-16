#!/usr/bin/env python3


class BasicCombatSkills:

    def __init__(self, **kwargs):
        '''
        Basic combat skills for the character

        Args:
            Passed by **kwargs
            sword: int - assigned value
                default value: 1
            axe: int - assigned value
                default value: 1
            blunt: int - assigned value
                default value: 1
            spear: int - assigned value
                default value: 1
            throw: int - assigned value
                default value: 1
            bow: int - assigned value
                default value: 1
            crossbow: int - assigned value
                default value: 1
        '''

        self.sword = kwargs.get('sword', 1)
        self.axe = kwargs.get('axe', 1)
        self.blunt = kwargs.get('blunt', 1)
        self.spear = kwargs.get('spear', 1)
        self.throw = kwargs.get('throw', 1)
        self.bow = kwargs.get('bow', 1)
        self.crossbow = kwargs.get('crossbow', 1)

    def show_combat_skills(self):
        '''
        Show assigned combat skills.

        Return:
             str - contains assigned attributes.
        '''

        return 'Sword:{}, Axe:{}, Blunt:{}, Spear:{}, Throw:{}, Bow:{}, Crossbow:{}'.format(
            self.sword,
            self.axe,
            self.blunt,
            self.spear,
            self.throw,
            self.bow,
            self.crossbow)