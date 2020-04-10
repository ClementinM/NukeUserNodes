# NukeUserNodes
Nuke: little script to load automaticaly user nodes and gizmos.

INSTALLATION
-
1. go to your `.nuke` folder:
    * Windows default: `C:\Users\{user}\.nuke`.
2. copy/paste the folder `user_nodes` inside `.nuke`.
3. `init.py` :
    * If `.nuke/init.py` does not exists, simple copy/paste the `init.py` of this package inside `.nuke`.
    * If `.nuke/init.py` already exists, add the content from the `init.py` of this package into the `.nuke/init.py`.


HOW TO USE
-
Simply add your `ToolName.nk` or `ToolName.gizmo` inside the user_nodes folder, then restart Nuke. They will be automaticaly loaded and added into a custom node menu.

You can also add a `ToolName.png` or `ToolName.jpg` to add an icon to your tool in the menu.
Adding a `menu.png` or `menu.jpg` will use it as the icon of the menu.

Your `.nuke` folder should look like this:
```
.nuke/
    init.py
    user_nodes/
        menu.py
        menu.png
        ProKeying.nk
        ProKeying.png
        ToolCool.nk
        ToolCool.png
        ...
```
---
2020-04-07, Clementin Massin
