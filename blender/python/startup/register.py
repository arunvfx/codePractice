import os.path
import sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append('/mnt/work/MyWorks/Pyscript/blender/pipeline/.venv/lib/python3.11/site-packages')
import eMenus
import eProperties
import eOperators
import ePanels


def register():
    print('register classes')
    eProperties.register()
    eOperators.register()
    ePanels.register()
    eMenus.topmenus.register()


def unregister():
    eMenus.topmenus.unregister()
    ePanels.unregister()
    eOperators.unregister()
    eProperties.unregister()


if __name__ == '__main__':
    register()
