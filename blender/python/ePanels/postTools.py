import bpy


class PostTools(bpy.types.Panel):
    bl_label = 'Post Tools'
    bl_idname = 'EDGE_PT_post_tools'
    bl_category = 'Post Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    name: bpy.props.StringProperty(name='Name', description='Enter the object name')

    def draw(self, context: 'Context'):
        layout = self.layout
        layout.label(text='Create Object')
        row = layout.row()
        # scene_ = bpy.context.scene

        object_property = context.scene.my_obj_properties

        row.prop(object_property, 'name')
        row = layout.row()
        row.prop(object_property, 'object')
        row = layout.row()
        row.prop(object_property, 'size')

        row = layout.row()
        row.operator('object.create_object', text=f'Create {object_property.object.capitalize()}')

