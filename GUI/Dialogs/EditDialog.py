from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QCheckBox,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
import sys
class EditDialog(QDialog):

	def __init__(self,cell):
		super(EditDialog, self).__init__()
		self.setWindowTitle("Edit Tag")
		self.layout = QVBoxLayout()
		self.line = QLineEdit(self)
		self.layout.addWidget(self.line)
		self.button = QPushButton('Apply', self)
		self.button.move(100,70)
		self.button.clicked.connect(lambda: self.on_click(cell))
		self.layout.addWidget(self.button)
		self.setLayout(self.layout)

	def on_click(self,cell):
		cell.setText(self.line.text())
		self.line.setText("")
		self.close()
