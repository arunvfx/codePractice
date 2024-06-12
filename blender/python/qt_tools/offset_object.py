import os.path

import bpy
from Qt import QtWidgets, QtCore, QtCompat


class OffsetObject(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        QtCompat.loadUi(uifile=f'{os.path.dirname(__file__)}/offset.ui', baseinstance=self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.x_slider.valueChanged.connect(self.offset_object)
        self.y_slider.valueChanged.connect(self.offset_object)
        self.z_slider.valueChanged.connect(self.offset_object)
        self.show()

    def offset_object(self):
        context = bpy.context
        if context.object is None:
            self.warning_message()
            return

        sender = self.sender()

        if sender.objectName() == 'x_slider':
            context.object.location.x = self.x_slider.value()

        elif sender.objectName() == 'y_slider':
            context.object.location.y = self.y_slider.value()

        elif sender.objectName() == 'z_slider':
            context.object.location.z = self.z_slider.value()

    def warning_message(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Failed!")
        dlg.setText("Select an object to offset")
        button = dlg.exec_()

        if button == QtWidgets.QMessageBox.Ok:
            print("OK!")


