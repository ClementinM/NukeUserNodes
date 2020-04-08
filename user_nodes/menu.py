"""
Adding a custom menu with all of the user nodes listed in the current folder.
- To add an icon to the menu, add an image in the current folder called "menu".
- To change the name of the menu, update MENU_NAME.
- You can add more image type support in the list TOOLS_ICONS_ACCEPTED, but not everything is supported by Nuke.
"""

import os
import nuke

MENU_NAME = 'User'
TOOLS_ICONS_ACCEPTED = ['.png', '.jpg', '.jpeg']
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_file_icon(file_name):
    for icon_ext in TOOLS_ICONS_ACCEPTED + [ext.upper() for ext in TOOLS_ICONS_ACCEPTED]:
        file_icon_path = os.path.join(CURRENT_DIR, '{}{}'.format(file_name, icon_ext))
        if os.path.exists(file_icon_path):
            return file_icon_path


print('Loading nodes menu "{}"...'.format(MENU_NAME))

nodes_menu = nuke.menu('Nodes')
user_nodes_menu = nodes_menu.addMenu(MENU_NAME, icon=get_file_icon('menu'))

list_files = os.listdir(CURRENT_DIR)
for f in sorted(list_files):
    f_name, f_ext = os.path.splitext(f)
    f_path = os.path.join(CURRENT_DIR, f)
    f_icon_path = get_file_icon(f_name)
    if f_ext == '.nk':
        user_nodes_menu.addCommand(f_name, 'nuke.loadToolset("{}")'.format(f_path), icon=f_icon_path)
    elif f_ext == '.gizmo':
        user_nodes_menu.addCommand(f_name, 'nuke.createNode("{}")'.format(f_name), icon=f_icon_path)