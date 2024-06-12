import typing

import bpy


class Test(bpy.types.Menu):
    bl_label = 'Edge'
    bl_idname = 'VIEW3D_MT_test'

    def draw(self, context: typing.Optional['Context']):
        layout = self.layout
        layout.operator(operator='mesh.primitive_cube_add', text='create cube')


class EdgeMenu(bpy.types.Menu):
    bl_label = 'Edge'
    bl_idname = 'VIEW3D_MT_edge_menu'

    def draw(self, context: typing.Optional['Context']):
        layout = self.layout
        row = layout.row(align=True)
        row.menu('VIEW3D_MT_test', text='Sub Menu')
        layout.operator(operator='mesh.primitive_cube_add', text='create cube')

    def add_menu(self, context):
        self.layout.menu(EdgeMenu.bl_idname)



bpy.utils.register_class(Test)
bpy.utils.register_class(EdgeMenu)
bpy.types.VIEW3D_MT_editor_menus.append(EdgeMenu.add_menu)
