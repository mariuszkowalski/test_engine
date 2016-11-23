#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from slot import Slot
from tkinter.ttk import Notebook
from random import randint as rnd
from hero import Hero
from items.basicweapon import BasicWeapon
from items.basicarmor import BasicArmor
from items.basicammo import BasicAmmo
from references import CHARACTER, SWORDS, AXES, BOWS, AMMO, ARMORS_HEAD, ARMORS_TORSO, ARMORS_BACK, ARMORS_ARMS,\
    ARMORS_LEGS, ARMORS_FEET
import os

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
        self._build_inventory_gui_layout()

        self.generate_basic_weapons_button = ttk.Button(self.inventory_debug_tab, text='generate wps')
        self.generate_basic_weapons_button.place(x=2, y=2)
        self.generate_basic_weapons_button.bind('<Button-1>', self.debug_generate_weapons)

        self.remove_basic_weapon_button = ttk.Button(self.inventory_debug_tab, text='remove b_a')
        self.remove_basic_weapon_button.place(x=82, y=2)
        self.remove_basic_weapon_button.bind('<Button-1>', self.debug_remove_weapon)

        self.generate_pick_up_item_button = ttk.Button(self.inventory_debug_tab, text='pick up')
        self.generate_pick_up_item_button.place(x=162, y=2)
        self.generate_pick_up_item_button.bind('<Button-1>', self.debug_pick_up_item)

        self.drop_item_button = ttk.Button(self.inventory_debug_tab, text='drop item')
        self.drop_item_button.place(x=242, y=2)
        self.drop_item_button.bind('<Button-1>', self.debug_drop_item)

        self.create_item_set_button = ttk.Button(self.inventory_debug_tab, text='create set')
        self.create_item_set_button.place(x=322, y=2)
        self.create_item_set_button.bind('<Button-1>', self.debug_create_item_set)

    def _build_inventory_gui_layout(self):
        # This could be built automatically.
        self.item_images = {
            'empty_slot': PhotoImage(file='items/images/empty_slot.png'),
            'battle_axe': PhotoImage(file='items/images/battle_axe.png'),
            'cloak': PhotoImage(file='items/images/cloak.png'),
            'hard_boots': PhotoImage(file='items/images/hard_boots.png'),
            'leather_armor': PhotoImage(file='items/images/leather_armor.png'),
            'leather_cap': PhotoImage(file='items/images/leather_cap.png'),
            'leather_gloves': PhotoImage(file='items/images/leather_gloves.png'),
            'rusty_short_sword': PhotoImage(file='items/images/rusty_short_sword.png'),
            'short_bow': PhotoImage(file='items/images/short_bow.png'),
            'thick_trousers': PhotoImage(file='items/images/thick_trousers.png'),
            'wooden_arrow': PhotoImage(file='items/images/wooden_arrow.png')
        }

        self.equipment_frame = ttk.LabelFrame(self.inventory_debug_tab, width=190, height=330, text='Equipment')
        self.equipment_frame.place(x=5, y=200)

        self.inventory_frame = ttk.LabelFrame(self.inventory_debug_tab, width=385, height=200, text='Inventory')
        self.inventory_frame.place(x=200, y=200)

        self.ground_frame = ttk.LabelFrame(self.inventory_debug_tab, width=385, height=120, text='Ground')
        self.ground_frame.place(x=200, y=400)

        #
        # Equipment slots.
        #
        self.inventory_slots = []
        self.inventory_slot_xy = []

        self.head_label_text = ttk.Label(self.equipment_frame, text='Head:')
        self.head_label_text.place(x=5, y=5)
        self.head_label_image = Slot(
            self.equipment_frame,
            slot_type='head',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.head_label_image.place(x=70, y=5)

        self.torso_label_text = ttk.Label(self.equipment_frame, text='Body:')
        self.torso_label_text.place(x=5, y=40)
        self.torso_label_image = Slot(
            self.equipment_frame,
            slot_type='body',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.torso_label_image.place(x=70, y=40)

        self.back_label_text = ttk.Label(self.equipment_frame, text='Back:')
        self.back_label_text.place(x=5, y=75)
        self.back_label_image = Slot(
            self.equipment_frame,
            slot_type='back',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.back_label_image.place(x=70, y=75)

        self.arms_label_text = ttk.Label(self.equipment_frame, text='Arms:')
        self.arms_label_text.place(x=5, y=110)
        self.arms_label_image = Slot(
            self.equipment_frame,
            slot_type='arms',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.arms_label_image.place(x=70, y=110)

        self.legs_label_text = ttk.Label(self.equipment_frame, text='Legs:')
        self.legs_label_text.place(x=5, y=145)
        self.legs_label_image = Slot(
            self.equipment_frame,
            slot_type='legs',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.legs_label_image.place(x=70, y=145)

        self.feet_label_text = ttk.Label(self.equipment_frame, text='Feet:')
        self.feet_label_text.place(x=5, y=180)
        self.feet_label_image = Slot(
            self.equipment_frame,
            slot_type='feet',
            item_name='None',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.feet_label_image.place(x=70, y=180)

        #
        #Create inventory grid. Using current tile size 32x32 the inventory grid is 10x5.
        #
        for i in range(50):
            rows_formula = 35 * (i // 10) #Y
            columns_formula = 35 * (i % 10) #X
            xy = [columns_formula, rows_formula]
            self.inventory_slot_xy.append(xy)

        self.inventory_slot_0 = Slot(
            self.inventory_frame,
            number=0,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_0.place(x=self.inventory_slot_xy[0][0], y=self.inventory_slot_xy[0][1])
        self.inventory_slot_0.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_0)

        self.inventory_slot_1 = Slot(
            self.inventory_frame,
            number=1,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_1.place(x=self.inventory_slot_xy[1][0], y=self.inventory_slot_xy[1][1])
        self.inventory_slot_1.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_1)

        self.inventory_slot_2 = Slot(
            self.inventory_frame,
            number=2,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_2.place(x=self.inventory_slot_xy[2][0], y=self.inventory_slot_xy[2][1])
        self.inventory_slot_2.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_2)

        self.inventory_slot_3 = Slot(
            self.inventory_frame,
            number=3,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_3.place(x=self.inventory_slot_xy[3][0], y=self.inventory_slot_xy[3][1])
        self.inventory_slot_3.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_3)

        self.inventory_slot_4 = Slot(
            self.inventory_frame,
            number=4,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_4.place(x=self.inventory_slot_xy[4][0], y=self.inventory_slot_xy[4][1])
        self.inventory_slot_4.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_4)

        self.inventory_slot_5 = Slot(
            self.inventory_frame,
            number=5,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_5.place(x=self.inventory_slot_xy[5][0], y=self.inventory_slot_xy[5][1])
        self.inventory_slot_5.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_5)

        self.inventory_slot_6 = Slot(
            self.inventory_frame,
            number=6,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_6.place(x=self.inventory_slot_xy[6][0], y=self.inventory_slot_xy[6][1])
        self.inventory_slot_6.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_6)

        self.inventory_slot_7 = Slot(
            self.inventory_frame,
            number=7,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_7.place(x=self.inventory_slot_xy[7][0], y=self.inventory_slot_xy[7][1])
        self.inventory_slot_7.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_7)

        self.inventory_slot_8 = Slot(
            self.inventory_frame,
            number=8,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_8.place(x=self.inventory_slot_xy[8][0], y=self.inventory_slot_xy[8][1])
        self.inventory_slot_8.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_8)

        self.inventory_slot_9 = Slot(
            self.inventory_frame,
            number=9,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_9.place(x=self.inventory_slot_xy[9][0], y=self.inventory_slot_xy[9][1])
        self.inventory_slot_9.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_9)

        self.inventory_slot_10 = Slot(
            self.inventory_frame,
            number=10,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_10.place(x=self.inventory_slot_xy[10][0], y=self.inventory_slot_xy[10][1])
        self.inventory_slot_10.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_10)

        self.inventory_slot_11 = Slot(
            self.inventory_frame,
            number=11,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_11.place(x=self.inventory_slot_xy[11][0], y=self.inventory_slot_xy[11][1])
        self.inventory_slot_11.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_11)

        self.inventory_slot_12 = Slot(
            self.inventory_frame,
            number=12,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_12.place(x=self.inventory_slot_xy[12][0], y=self.inventory_slot_xy[12][1])
        self.inventory_slot_12.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_12)

        self.inventory_slot_13 = Slot(
            self.inventory_frame,
            number=13,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_13.place(x=self.inventory_slot_xy[13][0], y=self.inventory_slot_xy[13][1])
        self.inventory_slot_13.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_13)

        self.inventory_slot_14 = Slot(
            self.inventory_frame,
            number=14,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_14.place(x=self.inventory_slot_xy[14][0], y=self.inventory_slot_xy[14][1])
        self.inventory_slot_14.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_14)

        self.inventory_slot_15 = Slot(
            self.inventory_frame,
            number=15,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_15.place(x=self.inventory_slot_xy[15][0], y=self.inventory_slot_xy[15][1])
        self.inventory_slot_15.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_15)

        self.inventory_slot_16 = Slot(
            self.inventory_frame,
            number=16,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_16.place(x=self.inventory_slot_xy[16][0], y=self.inventory_slot_xy[16][1])
        self.inventory_slot_16.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_16)

        self.inventory_slot_17 = Slot(
            self.inventory_frame,
            number=17,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_17.place(x=self.inventory_slot_xy[17][0], y=self.inventory_slot_xy[17][1])
        self.inventory_slot_17.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_17)

        self.inventory_slot_18 = Slot(
            self.inventory_frame,
            number=18,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_18.place(x=self.inventory_slot_xy[18][0], y=self.inventory_slot_xy[18][1])
        self.inventory_slot_18.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_18)

        self.inventory_slot_19 = Slot(
            self.inventory_frame,
            number=19,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_19.place(x=self.inventory_slot_xy[19][0], y=self.inventory_slot_xy[19][1])
        self.inventory_slot_19.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_19)

        self.inventory_slot_20 = Slot(
            self.inventory_frame,
            number=20,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_20.place(x=self.inventory_slot_xy[20][0], y=self.inventory_slot_xy[20][1])
        self.inventory_slot_20.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_20)

        self.inventory_slot_21 = Slot(
            self.inventory_frame,
            number=21,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_21.place(x=self.inventory_slot_xy[21][0], y=self.inventory_slot_xy[21][1])
        self.inventory_slot_21.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_21)

        self.inventory_slot_22 = Slot(
            self.inventory_frame,
            number=22,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_22.place(x=self.inventory_slot_xy[22][0], y=self.inventory_slot_xy[22][1])
        self.inventory_slot_22.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_22)

        self.inventory_slot_23 = Slot(
            self.inventory_frame,
            number=23,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_23.place(x=self.inventory_slot_xy[23][0], y=self.inventory_slot_xy[23][1])
        self.inventory_slot_23.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_23)

        self.inventory_slot_24 = Slot(
            self.inventory_frame,
            number=24,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_24.place(x=self.inventory_slot_xy[24][0], y=self.inventory_slot_xy[24][1])
        self.inventory_slot_24.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_24)

        self.inventory_slot_25 = Slot(
            self.inventory_frame,
            number=25,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_25.place(x=self.inventory_slot_xy[25][0], y=self.inventory_slot_xy[25][1])
        self.inventory_slot_25.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_25)

        self.inventory_slot_26 = Slot(
            self.inventory_frame,
            number=26,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_26.place(x=self.inventory_slot_xy[26][0], y=self.inventory_slot_xy[26][1])
        self.inventory_slot_26.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_26)

        self.inventory_slot_27 = Slot(
            self.inventory_frame,
            number=27,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_27.place(x=self.inventory_slot_xy[27][0], y=self.inventory_slot_xy[27][1])
        self.inventory_slot_27.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_27)

        self.inventory_slot_28 = Slot(
            self.inventory_frame,
            number=28,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_28.place(x=self.inventory_slot_xy[28][0], y=self.inventory_slot_xy[28][1])
        self.inventory_slot_28.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_28)

        self.inventory_slot_29 = Slot(
            self.inventory_frame,
            number=29,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_29.place(x=self.inventory_slot_xy[29][0], y=self.inventory_slot_xy[29][1])
        self.inventory_slot_29.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_29)

        self.inventory_slot_30 = Slot(
            self.inventory_frame,
            number=30,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_30.place(x=self.inventory_slot_xy[30][0], y=self.inventory_slot_xy[30][1])
        self.inventory_slot_30.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_30)

        self.inventory_slot_31 = Slot(
            self.inventory_frame,
            number=31,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_31.place(x=self.inventory_slot_xy[31][0], y=self.inventory_slot_xy[31][1])
        self.inventory_slot_31.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_31)

        self.inventory_slot_32 = Slot(
            self.inventory_frame,
            number=32,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_32.place(x=self.inventory_slot_xy[32][0], y=self.inventory_slot_xy[32][1])
        self.inventory_slot_32.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_32)

        self.inventory_slot_33 = Slot(
            self.inventory_frame,
            number=33,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_33.place(x=self.inventory_slot_xy[33][0], y=self.inventory_slot_xy[33][1])
        self.inventory_slot_33.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_33)

        self.inventory_slot_34 = Slot(
            self.inventory_frame,
            number=34,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_34.place(x=self.inventory_slot_xy[34][0], y=self.inventory_slot_xy[34][1])
        self.inventory_slot_34.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_34)

        self.inventory_slot_35 = Slot(
            self.inventory_frame,
            number=35,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_35.place(x=self.inventory_slot_xy[35][0], y=self.inventory_slot_xy[35][1])
        self.inventory_slot_35.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_35)

        self.inventory_slot_36 = Slot(
            self.inventory_frame,
            number=36,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_36.place(x=self.inventory_slot_xy[36][0], y=self.inventory_slot_xy[36][1])
        self.inventory_slot_36.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_36)

        self.inventory_slot_37 = Slot(
            self.inventory_frame,
            number=37,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_37.place(x=self.inventory_slot_xy[37][0], y=self.inventory_slot_xy[37][1])
        self.inventory_slot_37.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_37)

        self.inventory_slot_38 = Slot(
            self.inventory_frame,
            number=38,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_38.place(x=self.inventory_slot_xy[38][0], y=self.inventory_slot_xy[38][1])
        self.inventory_slot_38.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_38)

        self.inventory_slot_39 = Slot(
            self.inventory_frame,
            number=39,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_39.place(x=self.inventory_slot_xy[39][0], y=self.inventory_slot_xy[39][1])
        self.inventory_slot_39.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_39)

        self.inventory_slot_40 = Slot(
            self.inventory_frame,
            number=40,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_40.place(x=self.inventory_slot_xy[40][0], y=self.inventory_slot_xy[40][1])
        self.inventory_slot_40.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_40)

        self.inventory_slot_41 = Slot(
            self.inventory_frame,
            number=41,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_41.place(x=self.inventory_slot_xy[41][0], y=self.inventory_slot_xy[41][1])
        self.inventory_slot_41.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_41)

        self.inventory_slot_42 = Slot(
            self.inventory_frame,
            number=42,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_42.place(x=self.inventory_slot_xy[42][0], y=self.inventory_slot_xy[42][1])
        self.inventory_slot_42.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_42)

        self.inventory_slot_43 = Slot(
            self.inventory_frame,
            number=43,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_43.place(x=self.inventory_slot_xy[43][0], y=self.inventory_slot_xy[43][1])
        self.inventory_slot_43.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_43)

        self.inventory_slot_44 = Slot(
            self.inventory_frame,
            number=44,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_44.place(x=self.inventory_slot_xy[44][0], y=self.inventory_slot_xy[44][1])
        self.inventory_slot_44.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_44)

        self.inventory_slot_45 = Slot(
            self.inventory_frame,
            number=45,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_45.place(x=self.inventory_slot_xy[45][0], y=self.inventory_slot_xy[45][1])
        self.inventory_slot_45.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_45)

        self.inventory_slot_46 = Slot(
            self.inventory_frame,
            number=46,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_46.place(x=self.inventory_slot_xy[46][0], y=self.inventory_slot_xy[46][1])
        self.inventory_slot_46.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_46)

        self.inventory_slot_47 = Slot(
            self.inventory_frame,
            number=47,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_47.place(x=self.inventory_slot_xy[47][0], y=self.inventory_slot_xy[47][1])
        self.inventory_slot_47.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_47)

        self.inventory_slot_48 = Slot(
            self.inventory_frame,
            number=48,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_48.place(x=self.inventory_slot_xy[48][0], y=self.inventory_slot_xy[48][1])
        self.inventory_slot_48.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_48)

        self.inventory_slot_49 = Slot(
            self.inventory_frame,
            number=49,
            slot_type='inventory',
            image=self.item_images['empty_slot'],
            borderwidth=0,
            highlightthickness=0
        )
        self.inventory_slot_49.place(x=self.inventory_slot_xy[49][0], y=self.inventory_slot_xy[49][1])
        self.inventory_slot_49.bind('<Button-1>', self.inventory_slot_pressed)
        self.inventory_slots.append(self.inventory_slot_49)

    def _update_inventory_slots(self):
        for i in range(len(self.inventory_slots)):
            if i < len(self.hero.inventory.all):

                current_image = (self.hero.inventory.all[i].name).replace(' ', '_')
                item_name = self.hero.inventory.all[i].name
                self.inventory_slots[i].configure(image=self.item_images[current_image])
                self.inventory_slots[i].item_name = item_name

    def _update_equipment_slots(self):
        pass

    def inventory_slot_pressed(self):
        pass

    def inventory_slot_pressed(self, event):
        #
        # The last bind is active.
        #
        if self.inventory_slots[0] == self.inventory_slots[1]:
            print('what went wrong')
        else:
            print(vars(self.inventory_slots[0]))
            print(vars(self.inventory_slots[1]))

    #
    # Debug general methods.
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

    #
    # Debug stat methods.
    #
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

    #
    # Debug skill methods.
    #
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

    #
    # Debug inventory methods.
    #
    def debug_generate_weapons(self, event):
        basic_weapons = [
            BasicWeapon(**SWORDS['rusty short sword']),
            BasicWeapon(**SWORDS['excellent short sword']),
            BasicWeapon(**AXES['battle axe'])
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

    def debug_create_item_set(self, event):
        item_set = [
            BasicWeapon(**SWORDS['rusty short sword']),
            BasicWeapon(**AXES['battle axe']),
            BasicWeapon(**BOWS['short bow']),
            BasicArmor(**ARMORS_HEAD['leather cap']),
            BasicArmor(**ARMORS_TORSO['leather armor']),
            BasicArmor(**ARMORS_BACK['cloak']),
            BasicArmor(**ARMORS_ARMS['leather gloves']),
            BasicArmor(**ARMORS_LEGS['thick trousers']),
            BasicArmor(**ARMORS_FEET['hard boots']),
            BasicAmmo(**AMMO['wooden arrow'])
        ]

        for item in item_set:
            self.hero.pickup_item(item)
        print('Weight: {}, Items: {}'.format(self.hero.inventory.total_weight, self.hero.inventory.show_inventory()))
        self.hero.inventory.show_inventory_all()

        self._update_inventory_slots()

    #
    # Update important hero labels.
    #
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