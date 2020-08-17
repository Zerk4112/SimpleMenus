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

def test_func():
    main_menu.alert('Test','This is a test alert from slas.py')


main_menu = cli.Menu('~~ Main Menu ~~')
side_menu_01 = cli.Menu('~~ Side Menu 01 ~~')
side_menu_02 = cli.Menu('~~ Side Menu 02 ~~')

main_menu__option_1 = cli.Item('1 -- Side Menu 01', side_menu_01.start_prompt, main_menu)
main_menu__option_2 = cli.Item('2 -- Side Menu 02', side_menu_02.start_prompt, main_menu)
menu_menu__option_exit = cli.Item('3 -- Exit', main_menu.end_prompt, main_menu)
side_menu_01__option_01 = cli.Item('1 -- Test',test_func,side_menu_01)
side_menu_01__option_exit = cli.Item('2 -- Exit',side_menu_01.end_prompt,side_menu_01)
side_menu_02__option_exit = cli.Item('1 -- Exit',side_menu_02.end_prompt,side_menu_02)

cli.clear_screen()
main_menu.start_prompt()
