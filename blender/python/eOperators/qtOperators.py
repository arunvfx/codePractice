import os.path
import sys
import bpy
from PySide2 import QtWidgets, QtCore


def modal(self, context, event):
    wm = context.window_manager
    if not self.widget.isVisible():
        wm.event_timer_remove(self._timer)
        self.event_loop.exit(0)
        return {'FINISHED'}
    else:
        self.event_loop.processEvents()
        self.app.sendPostedEvents(None, 0)

    return {'PASS_THROUGH'}


def execute(self, context):
    self.app = QtWidgets.QApplication.instance()

    if not self.app:
        self.app = QtWidgets.QApplication(sys.argv )
        self.app.setStyle('fusion')
        load_stylesheet(self.app)

    self.event_loop = QtCore.QEventLoop()
    self.widget = getattr(self, 'qt_widget')()

    # run modal
    wm = context.window_manager
    self._timer = wm.event_timer_add(1 / 120, window=context.window)
    context.window_manager.modal_handler_add(self)

    return {'RUNNING_MODAL'}


def load_stylesheet(widget):
    stylesheet_file = f'{os.path.dirname(__file__)}/blender_stylesheet.qss'
    with open(stylesheet_file, 'r') as sf:
        widget.setStyleSheet(sf.read())


def poll(self, context):
    pass


def invoke(self, context):
    pass


def draw(self, context):
    pass


def operator_class(widget,
                   class_name,
                   bl_label,
                   bl_idname,
                   is_draw=False,
                   is_poll=False,
                   is_invoke=False,
                   is_modal=False):
    attributes = {'bl_label': bl_label,
                  'bl_idname': bl_idname,
                  'execute': execute,
                  'qt_widget': widget}

    if is_modal:
        attributes['modal'] = modal

    if is_poll:
        attributes['poll'] = poll

    if is_invoke:
        attributes['invoke'] = invoke

    if is_draw:
        attributes['draw'] = draw

    return type(class_name,
                (bpy.types.Operator,),
                attributes)
