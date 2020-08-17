import os
import time
from sys import platform


def clear_screen():
    if platform == "linux" or platform == "linux2":
        clear_screen_command = 'clear'
    elif platform == "darwin":
        clear_screen_command = 'cls'
    elif platform == "win32":
        clear_screen_command = 'cls'
    os.system(clear_screen_command)


class Menu:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []
        self.loop = True

    def add_item(self, item):
        self.items.append(item)
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
        self.loop = False

    def alert(self, title, message):
        clear_screen()
        print('!! ' + title + ' !!')
        print('- ' + message)
        input('Press Enter to continue ...')


    def start_prompt(self):
        self.loop = True
        while self.loop is True:
            clear_screen()
            self.draw()
            try:
                choice = int(input('Choose #: ')) - 1
                clear_screen()
                try:
                    self.items[choice].function()
                except IndexError:
                    self.alert('Choice Error','Invalid Choice - Try Again!')
            except ValueError:
                self.alert('Choice Error', 'Invalid Choice - Try Again!')


class Item:
    def __init__(self, name, function, parent=None):
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self)

    def draw(self):
        # might be more complex later, better use a method.
        print("    " + self.name)
