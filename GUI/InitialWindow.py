from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from Dialogs.TagPopup import TagPopup
from MainWindow.MainWindow import MainWindow

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
		self.openButton.clicked.connect(self.openFileNameDialog)
		# self.openButton.clicked.connect(self.openMainWindowUi)
		# self.openButton.clicked.connect(self.openPopup)
		self.TagPopup = TagPopup()
		self.MainWindowUi = MainWindow()

	#Instead of openPopup, this will be replaced with the main window. 
	def openPopup(self):        
		self.TagPopup.show()

	#Instead of openPopup, this will be replaced with the main window. 
	def openMainWindowUi(self):        
		self.MainWindowUi.show()

	#File manager open		
	def openFileManager(self):
		root = Tk() 
		root.geometry('200x100') 
		file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
		if file is not None: 
			content = file.read() 
			print(content) 

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			self.MainWindowUi.show()
			print(fileName)

	def openFileNamesDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
		if files:
			print(files)

	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
			print(fileName)



def window():
	app = QApplication(sys.argv)
	win = InitialWindow()
	win.show()
	sys.exit(app.exec_())


window()
