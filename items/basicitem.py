#!/usr/bin/env python3


class BasicItem:

    def __init__(self, name='', value=0, quantity=0, weight=0, **kwargs):
        self.name = name
        self.value = value
        self.quantity = quantity
        self.weight = weight
