from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
'''This file contains the window for the tag pop-up.'''
#TODO: Create a list in which appends the new tag everytime the user adds a new tag. 
#TODO: Save the user's tag input and display it on table
class TagPopup(QMainWindow):
	def __init__(self):
		super(TagPopup, self).__init__()
		self.resize(252, 310)
		self.initUI()

	def initUI(self):
		self.tagLabel = QtWidgets.QLabel(self)
		self.tagLabel.setGeometry(QtCore.QRect(20, 20, 71, 16))
		self.tagLabel.setText("Select Tag:")

		self.tagComboBox = QtWidgets.QComboBox(self)
		self.tagComboBox.setGeometry(QtCore.QRect(20, 30, 221, 51))

		self.newTagButton = QtWidgets.QPushButton(self)
		self.newTagButton.setGeometry(QtCore.QRect(20, 80, 113, 41))
		self.newTagButton.setText("Add New Tag")

		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(QtCore.QRect(20, 130, 211, 81))

		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QRect(40, 220, 164, 32))
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.cancelButton)

	#functionality for the cancelButton of the popUp window
	def cancelButton(self):
		self.close()


def openTagPopUp():
	app = QApplication(sys.argv)
	win = TagPopup()
	win.show()
	sys.exit(app.exec_())


# openTagPopUp()