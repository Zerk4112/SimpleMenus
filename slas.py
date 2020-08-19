import cli
import os, sys, time


def function_pass():
    print('Do nothing!?')
    pass


class Slas:
    def __init__(self):
        # Menus
        self.main_menu = cli.Menu('~~ Zachs Shitty Menus ~~')

        # Menu Options
        self.main_menu__option_1 = cli.Item(0,'1 -- Set Client Name. Current: None', self.setClientName, self.main_menu)
        self.main_menu__option_2 = cli.Item(1,'2 -- Set Server name. Current: None', self.setServerName,self.main_menu)
        self.main_menu__option_exit = cli.Item(2,'3 -- Exit',self.main_menu.end_prompt,self.main_menu)
        pass

    def setClientName(self):
        clientName = input('Enter a client name: ')
        self.main_menu__option_1 = cli.Item(0,f'1 -- Set Client Name. Current: {clientName}',self.setClientName,self.main_menu)
    def setServerName(self):
        serverName = input('Enter a server name: ')
        self.main_menu__option_2 = cli.Item(1,f'2 -- Set Server name. Current: {serverName}', self.setServerName,self.main_menu)



app = Slas()
app.main_menu.start_prompt()