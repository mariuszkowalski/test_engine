#!/usr/bin/env python3

from tkinter import Label


class Slot(Label):

    def __init__(self, master, number=0, slot_type='inventory', item_name='None',**kw):
        super().__init__(master, **kw)
        self.number = number
        self.slot_type = slot_type
        self.item_name = item_name
