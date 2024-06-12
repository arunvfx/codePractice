import sys
import bpy

from PySide2 import QtWidgets, QtCore


class PlanePanel(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(PlanePanel, self).__init__(parent=parent)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText('Enter the plane name here ...')
        self.button = QtWidgets.QPushButton('Create')
        self.layout().addWidget(self.line_edit)
        self.layout().addWidget(self.button)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.signals()
        self.show()

    def signals(self):
        self.button.clicked.connect(self.create_plane)

    def create_plane(self):
        bpy.ops.mesh.primitive_plane_add(size=3)

        text = self.line_edit.text()
        if text.strip():
            bpy.context.object.name = self.line_edit.text()

    def sizeHint(self):
        return QtCore.QSize(300, 300)
