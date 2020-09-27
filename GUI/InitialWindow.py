from tkinter import filedialog

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import tkinter as tk
from tkinter import *
from GUI.Dialogs.TagPopup import TagPopup

'''This file contains the Welcoming Window of the Visualization System.'''
#TODO: have the dialog to chose a folder working 
class InitialWindow(QMainWindow):
	def __init__(self):
		super(InitialWindow, self).__init__()
		self.setGeometry(200,200,300,300)
		self.resize(800, 600)
		self.setWindowTitle("Data Visualization System")
		self.initUI()

	def initUI(self):		
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Data Visualization System")
		self.label.setGeometry(QtCore.QRect(60, 30, 711, 101))
		font = QtGui.QFont()
		font.setPointSize(64)
		self.label.setFont(font)

		self.createNewButton = QtWidgets.QPushButton(self)
		self.createNewButton.setGeometry(QtCore.QRect(310, 330, 141, 32))
		self.createNewButton.setText("Create New Project")

		self.openButton = QtWidgets.QPushButton(self)
		self.openButton.setGeometry(QtCore.QRect(310, 270, 141, 32))
		self.openButton.setText("Open")
		self.openButton.clicked.connect(self.openPopup)

		self.TagPopup = TagPopup()


	#Instead of openPopup, this will be replaced with the main window. 
	def openPopup(self):        
		self.TagPopup.show()

	

	#File manager open		
	def openFileManager(self):
		root = tk.Tk()
		root.withdraw()

		file_path = filedialog.askopenfilename()


def window():
	app = QApplication(sys.argv)
	win = InitialWindow()
	win.show()
	sys.exit(app.exec_())


window()
