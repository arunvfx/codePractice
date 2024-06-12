import bpy


class ObjectProperties(bpy.types.PropertyGroup):

    object: bpy.props.EnumProperty(items=[
        ('cube', 'Cube', 'Create Cube Object'),
        ('plane', 'Plane', 'Create Plane Object')
    ],
        name='Object',
        description='Object type to create!')

    size: bpy.props.IntProperty(name='Size',
                                default=2,
                                min=1,
                                soft_max=6)
