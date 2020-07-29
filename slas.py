import cli
import os, sys, time
class Slas():
    def __init__(self):

        pass

fs_info = {}

def get_fs_info():
    print('FileSystem       Size  Used   Free   Use%   Mounted On')
    os.system('df -h | grep sda4')
    fs_info['file system'] = os.system("df -h | grep sda4 | tr -s ' ' ',' | cut -d, -f1 ")
    print('File System: ' + fs_info['file system'])



main_menu = cli.Menu('~~ Main Menu ~~')

main_menu__option_1 = cli.Item('1 -- Get FS Information',get_fs_info,main_menu)
menu_menu__option_exit = cli.Item('2 -- Exit',main_menu.end_prompt,main_menu)


cli.clear_screen()
main_menu.start_prompt()
