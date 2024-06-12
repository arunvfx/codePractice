import bpy

menuClassesToRegister = []
menus = {}


def draw(self, context):
    for menu_item, menu_operator in menus.get(self.__class__.__name__).items():
        self.layout.operator(menu_operator, text=menu_item)


def add_to_layout(self, context):
    for class_ in menuClassesToRegister:
        self.layout.menu(class_.bl_idname)


def add_menu():
    for menu_name, menu_items in menus.items():

        attributes = {
            'bl_idname': f'TOPBAR_MT_{menu_name.lower()}',
            'bl_label': menu_name,
            'draw': draw
        }

        menu_class = type(menu_name, (bpy.types.Menu,), attributes)
        menuClassesToRegister.append(menu_class)


def register():
    for class_ in menuClassesToRegister:
        bpy.utils.register_class(class_)

    bpy.types.TOPBAR_MT_editor_menus.append(add_to_layout)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(add_to_layout)
    for class_ in reversed(menuClassesToRegister):
        bpy.utils.unregister_class(class_)
