import bpy

from . import postTools, texturePanel


def register():
    bpy.utils.register_class(postTools.PostTools)


def unregister():
    bpy.utils.unregister_class(postTools.PostTools)
