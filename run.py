#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
from random import randint as rnd
from hero import Hero
from items.basicweapon import BasicWeapon
from references import CHARACTER, SWORDS, AXES


class Window:
    '''
    This is a debug class for the engine, for testing the behaviour of
    the implemented elements.
    '''

    def __init__(self, mainWidget):
        self.status_bar_text = StringVar()

        self.main_frame = ttk.Frame(mainWidget, width=800, height=580)
        self.main_frame.place(x=0, y=0)

        self.status_bar = ttk.Label(mainWidget, width=800, border=0, relief=SUNKEN, textvariable=self.status_bar_text)
        self.status_bar.place(x=0, y=580)

        self.build_main_gui()
        self.build_debug_gui()

    def build_main_gui(self):
        #Initialize hero.
        self.hero = Hero('Bradrick', **CHARACTER['sorcerer'])
        print(sorted(self.hero.show_all().items(), key=str))

        self.hero_name_label_text = StringVar()
        self.hero_hp_label_text = StringVar()
        self.hero_mp_label_text = StringVar()
        self.hero_lvl_label_text = StringVar()
        self.hero_xp_label_text = StringVar()
        self.hero_stat_points_label_text = StringVar()
        self.hero_skill_points_label_text = StringVar()

        self.hero_endurance_label_text = StringVar()
        self.hero_strength_label_text = StringVar()
        self.hero_agility_label_text = StringVar()
        self.hero_intelligence_label_text = StringVar()
        self.hero_wisdom_label_text = StringVar()

        self.hero_sword_skill_label_text = StringVar()
        self.hero_axe_skill_label_text = StringVar()
        self.hero_blunt_skill_label_text = StringVar()
        self.hero_spear_skill_label_text = StringVar()
        self.hero_throw_skill_label_text = StringVar()
        self.hero_bow_skill_label_text = StringVar()
        self.hero_crossbow_skill_label_text = StringVar()

        self.update_hero_labels()

        self.hero_frame = ttk.LabelFrame(self.main_frame, width=200, height=570, text='Hero')
        self.hero_frame.place(x=2, y=2)

        self.hero_name_label = ttk.Label(self.hero_frame, textvariable=self.hero_name_label_text)
        self.hero_name_label.place(x=2, y=2)

        self.hero_hp_label = ttk.Label(self.hero_frame, textvariable=self.hero_hp_label_text)
        self.hero_hp_label.place(x=2, y=22)

        self.hero_mp_label = ttk.Label(self.hero_frame, textvariable=self.hero_mp_label_text)
        self.hero_mp_label.place(x=2, y=42)

        self.hero_lvl_label = ttk.Label(self.hero_frame, textvariable=self.hero_lvl_label_text)
        self.hero_lvl_label.place(x=2, y=62)

        self.hero_xp_label = ttk.Label(self.hero_frame, textvariable=self.hero_xp_label_text)
        self.hero_xp_label.place(x=2, y=82)

        self.hero_stat_points_label = ttk.Label(self.hero_frame, textvariable=self.hero_stat_points_label_text)
        self.hero_stat_points_label.place(x=2, y=102)

        self.hero_skill_points_label = ttk.Label(self.hero_frame, textvariable=self.hero_skill_points_label_text)
        self.hero_skill_points_label.place(x=2, y=122)

        self.hero_strength_label = ttk.Label(self.hero_frame, textvariable=self.hero_strength_label_text)
        self.hero_strength_label.place(x=2, y=142)

        self.hero_endurance_label = ttk.Label(self.hero_frame, textvariable=self.hero_endurance_label_text)
        self.hero_endurance_label.place(x=2, y=162)

        self.hero_agility_label = ttk.Label(self.hero_frame, textvariable=self.hero_agility_label_text)
        self.hero_agility_label.place(x=2, y=182)

        self.hero_intelligence_label = ttk.Label(self.hero_frame, textvariable=self.hero_intelligence_label_text)
        self.hero_intelligence_label.place(x=2, y=202)

        self.hero_wisdom_label = ttk.Label(self.hero_frame, textvariable=self.hero_wisdom_label_text)
        self.hero_wisdom_label.place(x=2, y=222)

        self.hero_sword_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_sword_skill_label_text)
        self.hero_sword_skill_label.place(x=2, y=242)

        self.hero_axe_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_axe_skill_label_text)
        self.hero_axe_skill_label.place(x=2, y=262)

        self.hero_blunt_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_blunt_skill_label_text)
        self.hero_blunt_skill_label.place(x=2, y=282)

        self.hero_spear_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_spear_skill_label_text)
        self.hero_spear_skill_label.place(x=2, y=302)

        self.hero_throw_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_throw_skill_label_text)
        self.hero_throw_skill_label.place(x=2, y=322)

        self.hero_bow_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_bow_skill_label_text)
        self.hero_bow_skill_label.place(x=2, y=342)

        self.hero_crossbow_skill_label = ttk.Label(self.hero_frame, textvariable=self.hero_crossbow_skill_label_text)
        self.hero_crossbow_skill_label.place(x=2, y=362)

    def build_debug_gui(self):
        self.note = Notebook(self.main_frame)

        self.basic_debug_tab = ttk.Frame(self.note, width=590, height=535)
        self.inventory_debug_tab = ttk.Frame(self.note, width=590, height=535)

        self.note.add(self.basic_debug_tab, text='Basic Debug')
        self.note.add(self.inventory_debug_tab, text='Inventory Debug')
        self.note.place(x=204, y=10)

        self.build_basic_debug_buttons()
        self.build_stats_debug_buttons()
        self.build_combat_skills_debug_buttons()
        self.build_inventory_debug_buttons()

    def build_basic_debug_buttons(self):

        self.give_xp_button = ttk.Button(self.basic_debug_tab, text='give xp')
        self.give_xp_button.place(x=2, y=2)
        self.give_xp_button.bind('<Button-1>', self.debug_give_xp)

        self.give_small_xp_button = ttk.Button(self.basic_debug_tab, text='give small xp')
        self.give_small_xp_button.place(x=82, y=2)
        self.give_small_xp_button.bind('<Button-1>', self.debug_give_small_xp)

        self.take_hp_button = ttk.Button(self.basic_debug_tab, text='take hp')
        self.take_hp_button.place(x=2, y=32)
        self.take_hp_button.bind('<Button-1>', self.debug_take_hp)

        self.give_hp_button = ttk.Button(self.basic_debug_tab, text='give hp')
        self.give_hp_button.place(x=82, y=32)
        self.give_hp_button.bind('<Button-1>', self.debug_give_hp)

        self.take_mp_button = ttk.Button(self.basic_debug_tab, text='take mp')
        self.take_mp_button.place(x=162, y=32)
        self.take_mp_button.bind('<Button-1>', self.debug_take_mp)

        self.give_mp_button = ttk.Button(self.basic_debug_tab, text='give mp')
        self.give_mp_button.place(x=242, y=32)
        self.give_mp_button.bind('<Button-1>', self.debug_give_mp)

    def build_stats_debug_buttons(self):
        self.give_strength_button = ttk.Button(self.basic_debug_tab, text='give S')
        self.give_strength_button.place(x=2, y=62)
        self.give_strength_button.bind('<Button-1>', self.debug_give_strength)

        self.give_endurance_button = ttk.Button(self.basic_debug_tab, text='give E')
        self.give_endurance_button.place(x=82, y=62)
        self.give_endurance_button.bind('<Button-1>', self.debug_give_endurance)

        self.give_agility_button = ttk.Button(self.basic_debug_tab, text='give A')
        self.give_agility_button.place(x=162, y=62)
        self.give_agility_button.bind('<Button-1>', self.debug_give_agility)

        self.give_intelligence_button = ttk.Button(self.basic_debug_tab, text='give I')
        self.give_intelligence_button.place(x=242, y=62)
        self.give_intelligence_button.bind('<Button-1>', self.debug_give_intelligence)

        self.give_wisdom_button = ttk.Button(self.basic_debug_tab, text='give W')
        self.give_wisdom_button.place(x=322, y=62)
        self.give_wisdom_button.bind('<Button-1>', self.debug_give_wisdom)

    def build_combat_skills_debug_buttons(self):
        self.give_sword_skill_button = ttk.Button(self.basic_debug_tab, text='give sword')
        self.give_sword_skill_button.place(x=2, y=92)
        self.give_sword_skill_button.bind('<Button-1>', self.debug_give_sword_skill)

        self.give_axe_skill_button = ttk.Button(self.basic_debug_tab, text='give axe')
        self.give_axe_skill_button.place(x=82, y=92)
        self.give_axe_skill_button.bind('<Button-1>', self.debug_give_axe_skill)

        self.give_blunt_skill_button = ttk.Button(self.basic_debug_tab, text='give blunt')
        self.give_blunt_skill_button.place(x=162, y=92)
        self.give_blunt_skill_button.bind('<Button-1>', self.debug_give_blunt_skill)

        self.give_spear_skill_button = ttk.Button(self.basic_debug_tab, text='give spear')
        self.give_spear_skill_button.place(x=242, y=92)
        self.give_spear_skill_button.bind('<Button-1>', self.debug_give_spear_skill)

        self.give_throw_skill_button = ttk.Button(self.basic_debug_tab, text='give throw')
        self.give_throw_skill_button.place(x=322, y=92)
        self.give_throw_skill_button.bind('<Button-1>', self.debug_give_throw_skill)

        self.give_bow_skill_button = ttk.Button(self.basic_debug_tab, text='give bow')
        self.give_bow_skill_button.place(x=402, y=92)
        self.give_bow_skill_button.bind('<Button-1>', self.debug_give_bow_skill)

        self.give_crossbow_skill_button = ttk.Button(self.basic_debug_tab, text='give crossbow')
        self.give_crossbow_skill_button.place(x=482, y=92)
        self.give_crossbow_skill_button.bind('<Button-1>', self.debug_give_crossbow_skill)

    def build_inventory_debug_buttons(self):
        self.generate_basic_weapons_button = ttk.Button(self.inventory_debug_tab, text='generate wps')
        self.generate_basic_weapons_button.place(x=2, y=2)
        self.generate_basic_weapons_button.bind('<Button-1>', self.debug_generate_weapons)

        self.remove_basic_weapon_button = ttk.Button(self.inventory_debug_tab, text='remove b_a')
        self.remove_basic_weapon_button.place(x=82, y=2)
        self.remove_basic_weapon_button.bind('<Button-1>', self.debug_remove_weapon)

        self.generate_pick_up_item = ttk.Button(self.inventory_debug_tab, text='pick up')
        self.generate_pick_up_item.place(x=162, y=2)
        self.generate_pick_up_item.bind('<Button-1>', self.debug_pick_up_item)

        self.drop_item = ttk.Button(self.inventory_debug_tab, text='drop item')
        self.drop_item.place(x=242, y=2)
        self.drop_item.bind('<Button-1>', self.debug_drop_item)


    #
    # Debug methods.
    #
    def debug_give_xp(self, event):
        debug_value = rnd(1, 10) * 1000
        self.hero.xp += debug_value
        self.hero.check_xp()
        self.update_hero_labels()

    def debug_give_small_xp(self, event):
        debug_value = rnd(1, 20) * 10
        self.hero.xp += debug_value
        self.hero.check_xp()
        self.update_hero_labels()

    def debug_take_hp(self, event):
        self.hero.take_hp(12)
        self.update_hero_labels()

    def debug_give_hp(self, event):
        self.hero.give_hp(12)
        self.update_hero_labels()

    def debug_take_mp(self, event):
        self.hero.take_mp(12)
        self.update_hero_labels()

    def debug_give_mp(self, event):
        self.hero.give_mp(12)
        self.update_hero_labels()

    def debug_give_strength(self, event):
        self.hero.increase_stat('strength')
        self.update_hero_labels()

    def debug_give_endurance(self, event):
        self.hero.increase_stat('endurance')
        self.update_hero_labels()

    def debug_give_agility(self, event):
        self.hero.increase_stat('agility')
        self.update_hero_labels()

    def debug_give_intelligence(self, event):
        self.hero.increase_stat('intelligence')
        self.update_hero_labels()

    def debug_give_wisdom(self, event):
        self.hero.increase_stat('wisdom')
        self.update_hero_labels()

    def debug_give_sword_skill(self, event):
        self.hero.increase_combat_skill('sword')
        self.update_hero_labels()

    def debug_give_axe_skill(self, event):
        self.hero.increase_combat_skill('axe')
        self.update_hero_labels()

    def debug_give_blunt_skill(self, event):
        self.hero.increase_combat_skill('blunt')
        self.update_hero_labels()

    def debug_give_spear_skill(self, event):
        self.hero.increase_combat_skill('spear')
        self.update_hero_labels()

    def debug_give_throw_skill(self, event):
        self.hero.increase_combat_skill('throw')
        self.update_hero_labels()

    def debug_give_bow_skill(self, event):
        self.hero.increase_combat_skill('bow')
        self.update_hero_labels()

    def debug_give_crossbow_skill(self, event):
        self.hero.increase_combat_skill('crossbow')
        self.update_hero_labels()

    def debug_generate_weapons(self, event):
        basic_weapons = [
            BasicWeapon(**SWORDS['rusty short sword']),
            BasicWeapon(**SWORDS['excellent short sword']),
            BasicWeapon(**AXES['axes']['battle axe'])
        ]

        item_to_move = basic_weapons.pop(rnd(0, 2))

        self.hero.inventory.add_to_inventory(item_to_move)
        print('Weight: {}, Items: {}'.format(self.hero.inventory.total_weight, self.hero.inventory.show_inventory()))
        self.hero.inventory.show_inventory_all()

    def debug_remove_weapon(self, event):
        item = 'battle axe'

        self.hero.inventory.remove_from_inventory(item)
        print('Weight: {}, Items: {}'.format(self.hero.inventory.total_weight, self.hero.inventory.show_inventory()))
        self.hero.inventory.show_inventory_all()

    def debug_pick_up_item(self, event):
        basic_weapons = [
            BasicWeapon(**SWORDS['rusty short sword']),
            BasicWeapon(**SWORDS['excellent short sword']),
            BasicWeapon(**AXES['battle axe'])
        ]

        item_to_move = basic_weapons.pop(rnd(0, 2))

        self.hero.pickup_item(item_to_move)
        print('Weight: {}, Items: {}'.format(self.hero.inventory.total_weight, self.hero.inventory.show_inventory()))
        self.hero.inventory.show_inventory_all()

    def debug_drop_item(self, event):
        item = 'battle axe'

        self.hero.drop_item(item)
        print('Weight: {}, Items: {}'.format(self.hero.inventory.total_weight, self.hero.inventory.show_inventory()))
        self.hero.inventory.show_inventory_all()

    def update_hero_labels(self):
        self.hero_name_label_text.set('Name: {}'.format(self.hero.name))
        self.hero_hp_label_text.set('HP: {}/{}'.format(self.hero.current_hp, self.hero.max_hp))
        self.hero_mp_label_text.set('MP: {}/{}'.format(self.hero.current_mp, self.hero.max_mp))
        self.hero_lvl_label_text.set('Level: {}'.format(self.hero.lvl))
        self.hero_xp_label_text.set('Current XP: {}'.format(self.hero.xp))
        self.hero_stat_points_label_text.set('Stat points: {}'.format(self.hero.stat_points))
        self.hero_skill_points_label_text.set('Skill points: {}'.format(self.hero.skill_points))

        self.hero_strength_label_text.set('Strength: {}'.format(self.hero.stats.strength))
        self.hero_endurance_label_text.set('Endurance: {}'.format(self.hero.stats.endurance))
        self.hero_agility_label_text.set('Agility: {}'.format(self.hero.stats.agility))
        self.hero_intelligence_label_text.set('Intelligence: {}'.format(self.hero.stats.intelligence))
        self.hero_wisdom_label_text.set('Wisdom: {}'.format(self.hero.stats.wisdom))

        self.hero_sword_skill_label_text.set('Sword: {}'.format(self.hero.combat_skills.sword))
        self.hero_axe_skill_label_text.set('Axe: {}'.format(self.hero.combat_skills.axe))
        self.hero_blunt_skill_label_text.set('Blunt: {}'.format(self.hero.combat_skills.blunt))
        self.hero_spear_skill_label_text.set('Spear: {}'.format(self.hero.combat_skills.spear))
        self.hero_throw_skill_label_text.set('Throw: {}'.format(self.hero.combat_skills.throw))
        self.hero_bow_skill_label_text.set('Bow: {}'.format(self.hero.combat_skills.bow))
        self.hero_crossbow_skill_label_text.set('Crossbow: {}'.format(self.hero.combat_skills.crossbow))


def main():
    global root
    root = Tk()
    root.title('Engine test')
    root.geometry('800x600+50+50')
    root.resizable(width=0, height=0)

    window = Window(root)

    root.mainloop()


if __name__ == '__main__':
    main()