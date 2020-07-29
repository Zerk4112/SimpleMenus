import os, sys
import time
def clear_screen():
    os.system('clear')
class Menu:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []
        self.loop = True
        self.alertTrap = True
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
        self.alertTrap = True
        self.loop = False

    def alert(self,title,message):
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
                    if self.alertTrap is False:
                        input('\nPress Enter to Continue ...')
                    else:
                        self.alertTrap = False
                except IndexError:
                    print('Invalid Choice - Try again!')
            except ValueError:
                clear_screen()
                print('Invalid Choice - Try Again!')


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