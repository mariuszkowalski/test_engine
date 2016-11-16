#!/usr/bin/env python3


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

ITEMS = {
    'swords': {
        'rusty short sword': {
            'name': 'rusty short sword',
            'family': 'sword',
            'damage': (1, 3),
            'pierce': 5,
            'value': 5,
            'quantity': 1,
            'weight': 3,
        },
        'excellent short sword': {
            'name': 'excellent short sword',
            'family': 'sword',
            'damage': (5, 10),
            'pierce': 10,
            'value': 125,
            'quantity': 1,
            'weight': 4,
        },
    },
    'axes': {
        'battle axe': {
            'name': 'battle axe',
            'family': 'axe',
            'damage': (10, 25),
            'pierce': 15,
            'value': 50,
            'quantity': 1,
            'weight': 3,
        }
    }
}
