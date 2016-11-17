#!/usr/bin/env python3


from basiccharacter import BasicCharacter


class Hero(BasicCharacter):

    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        '''
        Hero class is main character class.

        Args:
            name: str - name of the hero
            *args: different parameters - not used
            **kwargs: dict - passed to initialize inherited classes and instances

        Default attributes:
            xp: int - experience points earn by the hero
            lvl: int - current level of the hero
            stat_points: int - number of points to increase stats
            skill_points: int - number of points to increase skills
            stat_points_on_lvl: int - number of stat points earned at level up
                default value: 4

        Traits:
            Derivatives of the many different attributes.
            hp_on_lvl: int - number of hp points gained on each level
            mp_on_lvl: int - number of mp points gained on each level
            skill_points_on_lvl: int - number of skill points gained on each level
            unarmed_attack - damage of unarmed attack
            dodge - chance of the doge of the enemy attack
            basic_m_defence - number if the m_defence
        '''

        self.xp = 0
        self.lvl = 1

        self.stat_points = 0
        self.skill_points = 0
        self.stat_points_on_lvl = 4

        # To recalculate after points assignment.
        self._calculate_traits()

    def check_xp(self):
        '''
        Check it level up is available for character.
        '''

        do_check = True

        while do_check:
            xp_need = ((self.lvl + 1) * 1000) - 1000

            if self.xp >= xp_need:
                self.lvl += 1
                self.max_hp += self.hp_on_lvl
                self.max_mp += self.mp_on_lvl
                self.current_hp += self.hp_on_lvl
                self.current_mp += self.mp_on_lvl
                self.stat_points += self.stat_points_on_lvl
                self.skill_points += self.skill_points_on_lvl
                self.xp -= xp_need

            else:
                do_check = False

    def increase_stat(self, stat_name):
        '''
        Increase stat by value of 1

        Args:
            stat_name: str - passed stat name
                Viable options: strength, endurance, intelligence, agility, wisdom
        '''

        if self.stat_points > 0:

            if stat_name == 'strength':
                self.stats.strength += 1

            elif stat_name == 'endurance':
                self.stats.endurance += 1

            elif stat_name == 'agility':
                self.stats.agility += 1

            elif stat_name == 'intelligence':
                self.stats.intelligence += 1

            elif stat_name == 'wisdom':
                self.stats.wisdom += 1

            self.stat_points -= 1
            self._calculate_traits()

    def increase_combat_skill(self, skill_name):
        '''
        Increase combat skill by value of 1

        Args:
            skill_name: str - passed skill name
                Viable options: sword, axe, blunt, spear, throw, bow, crossbow
        '''

        if self.skill_points > 0:

            if skill_name == 'sword':
                self.combat_skills.sword += 1

            elif skill_name == 'axe':
                self.combat_skills.axe += 1

            elif skill_name == 'blunt':
                self.combat_skills.blunt += 1

            elif skill_name == 'spear':
                self.combat_skills.spear += 1

            elif skill_name == 'throw':
                self.combat_skills.throw += 1

            elif skill_name == 'bow':
                self.combat_skills.bow += 1

            elif skill_name == 'crossbow':
                self.combat_skills.crossbow += 1

            self.skill_points -= 1
            self._calculate_traits()

    def pickup_item(self, item_instance):
        '''
        This method checks what the total weight of the inventory would be after
        adding another item. If the mass would be less than carry max of the character
        the item is added to the inventory list.

        Args:
              item_instance: obj - valid instance of the class derived from the BasicItem class.
        '''

        future_weight = self.inventory.total_weight + item_instance.weight

        if future_weight < self.carry_max:
            self.inventory.add_to_inventory(item_instance)


    def drop_item(self, item_name):
        '''
        This method removes the item from the inventory.
        There is no check against target inventory cary max.

        Args:
            item_name: str - name of the item to drop.
        '''

        self.inventory.remove_from_inventory(item_name)

    def _calculate_traits(self):
        '''
        Calculates different traits of the character which could change after
        changing the stat points.
        '''

        self.hp_on_lvl = self.stats.endurance
        self.mp_on_lvl = self.stats.wisdom
        self.carry_max = 5 * self.stats.strength
        self.skill_points_on_lvl = int(10 + 0.1 * self.stats.intelligence)

        self.unarmed_attack = int(0.5 * self.stats.strength + 0.25 * self.stats.agility)
        self.dodge = int(1 * self.stats.agility + 0.5 * self.stats.endurance)
        self.basic_m_defence = int(1 * self.stats.wisdom + 0.5 * self.stats.endurance)

    def show_all(self):
        '''
        Show all variables in the class.

        Return:
            dict - all the variables present in the class.
        '''

        return vars(self)
