import bpy

from . import createObjProps

classes = {
    bpy.types.Scene: ('my_obj_properties', createObjProps.ObjectProperties)
}


def register():
    print('Register Properties')
    for data_block, prop in classes.items():
        attribute_name, prop_class = prop
        bpy.utils.register_class(prop_class)
        setattr(data_block, attribute_name, bpy.props.PointerProperty(type=prop_class))


def unregister():
    print('Unregister Properties')

    for data_block, prop in classes.items():
        attribute_name, prop_class = prop
        bpy.utils.unregister_class(prop_class)
        delattr(data_block, attribute_name)
