import sys
import bpy

from PySide2 import QtWidgets, QtCore


class CubePanel(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(CubePanel, self).__init__(parent=parent)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.button = QtWidgets.QPushButton('Hia')
        self.layout().addWidget(self.button)
        self.signals()
        self.show()
        self.button.setFocusPolicy(QtCore.Qt.ClickFocus)

    def signals(self):
        self.button.clicked.connect(self.create_cube)

    def create_cube(self):
        bpy.ops.mesh.primitive_cube_add(size=3)

    def sizeHint(self):
        return QtCore.QSize(300, 300)
