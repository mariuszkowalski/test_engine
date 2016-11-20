#!/usr/bin/env python3

#
# File with the references used ass arguments passed to the classes constructors.
#


CHARACTER = {
    'knight': {
        'strength': 30,
        'endurance': 30,
        'agility': 20,
        'intelligence': 15,
        'wisdom': 10,
        'sword': 50,
        'axe': 15,
        'blunt': 45,
        'spear': 50,
        'throw': 15,
        'bow': 40,
        'crossbow': 30
        },
    'sorcerer': {
        'strength': 10,
        'endurance': 15,
        'agility': 15,
        'intelligence': 35,
        'wisdom': 30,
        'sword': 5,
        'axe': 5,
        'blunt': 30,
        'spear': 5,
        'throw': 25,
        'bow': 15,
        'crossbow': 5
    }
}

#
# Items weapons.
#
# Valid weapon types - sword, axe, blunt, spear, throw, bow, crossbow;
# corresponds to the basicscombatkills class.
#
SWORDS= {
    'rusty short sword': {
        'name': 'rusty short sword',
        'family': 'sword',
        'hands': 'one',
        'damage': (1, 3),
        'pierce': 5,
        'value': 5,
        'quantity': 1,
        'weight': 4,
    },
    'excellent short sword': {
        'name': 'excellent short sword',
        'family': 'sword',
        'hands': 'one',
        'damage': (5, 10),
        'pierce': 10,
        'value': 125,
        'quantity': 1,
        'weight': 3,
    },
}

AXES = {
    'battle axe': {
        'name': 'battle axe',
        'family': 'axe',
        'hands': 'two',
        'damage': (10, 25),
        'pierce': 15,
        'value': 50,
        'quantity': 1,
        'weight': 9,
    }
}

BOWS = {
    'short bow': {
        'name': 'short bow',
        'family': 'bow',
        'hands': 'two',
        'damage': (4, 8),
        'pierce': 30,
        'value': 25,
        'quantity': 1,
        'weight': 2,
    }
}

AMMO = {
    'wooden arrow': {
        'name': 'wooden arrow',
        'family': 'arrow',
        'damage_bonus': (1, 2),
        'pierce': 5,
        'value': 1,
        'quantity': 10,
        'weight': 0
    }
}

#
# Items armors
#
# Valid armor types 'family' - head, torso, back, arms, legs, feet;
# corresponds to he basicequipment class.
#
ARMORS_TORSO = {
    'leather armor': {
        'name': 'leather armor',
        'family': 'torso',
        'damage_protection': 4,
        'damage_disperse': 5,
        'value': 25,
        'quantity': 1,
        'weight': 4
    }
}

ARMORS_HEAD = {
    'leather cap': {
        'name': 'leather cap',
        'family': 'head',
        'damage_protection': 1,
        'damage_disperse': 5,
        'value': 5,
        'quantity': 1,
        'weight': 1
    }
}

ARMORS_BACK = {
    'cloak': {
        'name': 'cloak',
        'family': 'back',
        'damage_protection': 2,
        'damage_disperse': 5,
        'value': 15,
        'quantity': 1,
        'weight': 2
    }
}

ARMORS_ARMS = {
    'leather gloves': {
        'name': 'leather gloves',
        'family': 'arms',
        'damage_protection': 1,
        'damage_disperse': 5,
        'value': 5,
        'quantity': 1,
        'weight': 2
    }
}

ARMORS_LEGS = {
    'thick trousers': {
        'name': 'thick trousers',
        'family': 'legs',
        'damage_protection': 2,
        'damage_disperse': 5,
        'value': 10,
        'quantity': 1,
        'weight': 2
    }
}

ARMORS_FEET = {
    'hard boots': {
        'name': 'hard boots',
        'family': 'back',
        'damage_protection': 3,
        'damage_disperse': 5,
        'value': 15,
        'quantity': 1,
        'weight': 2
    }
}