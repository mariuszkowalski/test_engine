#!/usr/bin/env python3


from basicinventory import BasicInventory


class CharacterInventory(BasicInventory):

    def __init__(self):
        super().__init__()
        self.total_weight = 0

    def _calculate_total_weight(self):
        '''
        Calculate total weight of all items in the inventory.
        '''

        if len(self.all) > 0:
            for item in self.all:

                if item.quantity > 1:
                    self.total_weight += item.quantity * item.weight
                elif item.quantity == 1:
                    self.total_weight += item.weight

    def add_to_inventory(self, current_item):
        '''
        Adds current item to the inventory list.

        Args:
            current_item: instance - instance of the valid item class.
        '''

        increased_quantity = False
        if len(self.all) == 0:
            self.all.append(current_item)
            self.total_weight += current_item.weight

        elif len(self.all) >= 1:

            for item in self.all:

                if item.name == current_item.name:
                    item.quantity += current_item.quantity
                    self.total_weight += current_item.weight * current_item.quantity
                    increased_quantity = True

            if not increased_quantity:
                self.all.append(current_item)
                self.total_weight += current_item.weight


    def remove_from_inventory(self, current_name):
        '''
        Removes item from the inventory list using name of the item, if there is more items than
        one quantity of given item is decreased.

        Args:
            current_name: str - string name of the item.
        '''

        if len(self.all) > 0:

            for i, item in enumerate(self.all):

                if item.name == current_name:

                    if item.quantity == 1:
                        self.all.pop(i)
                        self.total_weight -= item.weight
                    else:
                        item.quantity -= 1
                        self.total_weight -= item.weight