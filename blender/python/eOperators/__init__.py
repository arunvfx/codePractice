import bpy

from . import objOperators

classes = (objOperators.Wireframe,
           objOperators.CreateObject,
           objOperators.create_cube_op(),
           objOperators.create_plane_op(),
           objOperators.offset_object_op())


def register():
    for operator in classes:
        bpy.utils.register_class(operator)


def unregister():
    for operator in reversed(classes):
        bpy.utils.unregister_class(operator)
