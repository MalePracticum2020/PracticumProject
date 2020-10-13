from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)
import sys, os, subprocess, platform
from pip._internal.utils import logging
from GUI.Dialogs.TagPopup import TagPopup
from GUI.MainWindow.MainWindow import MainWindow

'''This file contains the Welcoming Window of the Visualization System.'''
#TODO: Synchronize the packet view -> timeline view and vice versa
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
		self.label.setGeometry(QtCore.QRect(150, 30, 711, 101))
		font = QtGui.QFont()
		font.setPointSize(30)
		self.label.setFont(font)

		self.createNewButton = QtWidgets.QPushButton(self)
		self.createNewButton.setGeometry(QtCore.QRect(310, 330, 141, 32))
		self.createNewButton.setText("Create New Project")
		self.createNewButton.clicked.connect(self.openFileNameDialog)

		self.openButton = QtWidgets.QPushButton(self)
		self.openButton.setGeometry(QtCore.QRect(310, 270, 141, 32))
		self.openButton.setText("Open")
		self.openButton.clicked.connect(self.openFileEvent)
		# self.openButton.clicked.connect(self.openMainWindowUi)
		self.TagPopup = TagPopup()
		# self.MainWindowUi = MainWindow("")
	#Instead of openPopup, this will be replaced with the main window. 
	def openPopup(self):        
		self.TagPopup.show()

	#Instead of openPopup, this will be replaced with the main window. 
	def openMainWindowUi(self):        
		self.MainWindowUi.show()

	#File manager to open pcap file in wireshark and timeline view
	def openFileEvent(self):

			# Ask user if they want to import file or dir
			import_type = QMessageBox.question(self,
											   "Open",
											   "Do you want to import a .pcap file?",
											   QMessageBox.Yes | QMessageBox.No)

			if import_type == QMessageBox.Yes:
				pcap_file = QFileDialog()
				filenames, _ = QFileDialog.getOpenFileNames(pcap_file, "Select File")

				if len(filenames) < 0:
					logging.debug("File choose cancelled")
					return

				if len(filenames) > 0:
					self.pcap_to_import = filenames[0]
					if platform.system() == 'Darwin':  # macOS
						subprocess.call(('open', self.pcap_to_import ))
					elif platform.system() == 'Windows':  # Windows
						os.startfile(self.pcap_to_import )
					else:  # linux variants
						subprocess.call(('xdg-open', self.pcap_to_import ))

	def openFileNameDialog(self):
		dialog = QFileDialog()
		folder_path = dialog.getExistingDirectory(None, "Select Folder")
		if folder_path:
			self.MainWindowUi = MainWindow(folder_path)
			self.openMainWindowUi()



def window():
	app = QApplication(sys.argv)
	win = InitialWindow()
	win.show()
	sys.exit(app.exec_())


window()
