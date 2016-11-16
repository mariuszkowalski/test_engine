#!/usr/bin/env python3


class BasicStats:

    def __init__(self, **kwargs):
        '''
        Basic stats for the character.

        Args:
            Passed by **kwargs.
            strength: int - assigned value
                default value: 10
            endurance: int - assigned value
                default value: 10
            agility: int - assigned value
                default value: 10
            intelligence: int - assigned value
                default value: 10
            wisdom: int - assigned value
                default value: 10
        '''

        self.strength = kwargs.get('strength', 10)
        self.endurance = kwargs.get('endurance', 10)
        self.agility = kwargs.get('agility', 10)
        self.intelligence = kwargs.get('intelligence', 10)
        self.wisdom = kwargs.get('wisdom', 10)

    def show_stats(self):
        '''
        Show assigned stats.

        Return:
             str - contains assigned attributes.
        '''

        return 'S:{}, E:{}, A:{}, I:{}, W:{}'.format(
            self.strength,
            self.endurance,
            self.agility,
            self.intelligence,
            self.wisdom)