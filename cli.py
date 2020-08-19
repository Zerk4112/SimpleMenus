import os, sys
import time
# last updated 8/18/2020


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


class Menu():
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []
        self.loop = True
        self.alertTrap = True

    def add_item(self, item, itemID):
        print(self.items)
        for list_item in self.items:
            if itemID == list_item.id:
                self.find_check = True
                break
            else:
                self.find_check = False
        if len(self.items) == 0:
            self.find_check = False
        if self.find_check is False:
                self.items.append(item)
        else:
            self.items.remove(list_item)
            self.items.insert(itemID, item)

        if item.parent != self:
            item.parent = self

    def remove_item(self, item):
        self.items.remove(item)
        if item.parent == self:
            item.parent = None

    def draw(self):
        print(self.name)
        for item in self.items:
            item.draw()

    def end_prompt(self):
        self.alertTrap = True
        self.loop = False

    def alert(self, title, message):
        self.alertTrap = True
        clear_screen()
        print('!! ' + title + ' !!')
        print('- ' + message)
        input('Press Enter to continue ...')
        clear_screen()

    def start_prompt(self):
        self.loop = True
        while self.loop is True:
            self.draw()
            try:
                choice = int(input('Choose #: ')) - 1
                clear_screen()
                try:
                    self.items[choice].function()
                except IndexError:
                    print('Invalid Choice - Try again!')
            except ValueError:
                clear_screen()
                print('Invalid Choice - Try Again!')


class Item():
    def __init__(self, itemID, name, function, parent=None):
        self.id = itemID
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self, itemID)

    def draw(self):
        # might be more complex later, better use a method.
        print("    " + self.name)
