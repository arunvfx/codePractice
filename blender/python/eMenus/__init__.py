from . import topmenus, view3dMenus

menus = {
    'Edge': {
        'Convert to Wireframe': 'object.wireframe',
        'Smooth Object': 'object.shade_smooth',
        'Qt Widget': 'edge.pyside_panel',
        'Create Plane': 'edge.create_plane',
        'Offset Object': 'edge.offset_object'
    },
    'Studio': {
        'Select All': 'object.select_all'
    }
}

topmenus.menus = menus
topmenus.add_menu()

# bpy.ops.wm.call_menu(name=EdgeMenu.bl_idname)
