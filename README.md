# Nuke: UserNodes
Little script to load automaticaly user nodes and gizmos.

[![project_foundry_nuke](https://img.shields.io/badge/my%20category-foundry--nuke-orange?style=flat-square)](https://github.com/ClementinM?tab=repositories&q=%23foundry-nuke&type=&language=)
[![project_vfx_pipeline](https://img.shields.io/badge/my%20category-vfx--pipeline-brightgreen?style=flat-square)](https://github.com/ClementinM?tab=repositories&q=%23vfx-pipeline&type=&language=)

Download
-
[![latest_stable](https://img.shields.io/github/v/release/ClementinM/NukeUserNodes?label=latest%20release&style=flat-square)](https://github.com/ClementinM/NukeUserNodes/releases/latest)

Installation
-
1. Go to your `.nuke` folder:
    * Windows: `C:\Users\{user}\.nuke`
    * Linux & Mac: `/home/{user}/.nuke`
2. Copy/paste the folder `user_nodes` of this package inside `.nuke`.
4. `init.py`:
    * If `.nuke/init.py` does not exists, simple copy/paste the `init.py` of this package inside `.nuke`.
    * If `.nuke/init.py` already exists, add the content from the `init.py` of this package into the `.nuke/init.py`.
5. Voila!

How to use
-
Simply add your `ToolName.nk` or `ToolName.gizmo` inside the `user_nodes` folder, then restart Nuke if already open.
They will be automaticaly loaded and added into a custom node menu.

* Adding a `menu.png` or `menu.jpg` will use it as the icon of the menu.
* You can also add a `ToolName.png` or `ToolName.jpg` to add an icon to your tool in the menu (exact same name than the tool itself).

Example:
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

Advice: live group vs gizmo
-
I suggest to use only live groups `.nk` for simple/stand-alone tools, and using gizmo `.gizmo` only for tool using external source code for example.

To convert a gizmo into a group, change the file ext `.gizmo` by `.nk` and edit the top part `Gizmo {` by `Group {`.

Live groups can be copied/pasted easily, and a nuke script using them can be opened from anywhere. Gizmos can't be used if you didn't installed it (like with this tool), so if you send a nuke script to someone else, this person will not be able to open it correctly without installing the gizmo.
Also, live groups allow users to see what's happening inside the tools, it's more instructive :-)

Contact
-
[Clementin Massin](https://www.linkedin.com/in/clementinmassin)
