import bpy
from . import qtOperators
from qt_tools import create_plane, create_cube, offset_object


class Wireframe(bpy.types.Operator):
    bl_idname = 'object.wireframe'
    bl_label = 'Wireframe'

    @classmethod
    def poll(cls, context: 'Context') -> bool:
        if bpy.context.object is not None:
            return True

        return False

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.wireframe(thickness=0.1)
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}


class CreateObject(bpy.types.Operator):
    bl_idname = 'object.create_object'
    bl_label = 'create object'

    def execute(self, context):
        object_property = context.scene.my_obj_properties

        if object_property.object == 'cube':
            bpy.ops.mesh.primitive_cube_add(size=object_property.size)

        elif object_property.object == 'plane':
            bpy.ops.mesh.primitive_plane_add(size=object_property.size)

        context.object.name = object_property.name

        return {'FINISHED'}


def create_cube_op():
    return qtOperators.operator_class(
        create_cube.CubePanel,
        'CreateCube',
        bl_label='Create Cube',
        bl_idname='edge.create_cube',
        is_modal=True
    )


def create_plane_op():
    return qtOperators.operator_class(
        create_plane.PlanePanel,
        'CreatePlane',
        bl_label='Create Plane',
        bl_idname='edge.create_plane',
        is_modal=True
    )


def offset_object_op():
    return qtOperators.operator_class(
        offset_object.OffsetObject,
        'OffsetObject',
        bl_label='Offset object',
        bl_idname='edge.offset_object',
        is_modal=True
    )
