from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)
import sys, subprocess, os, platform
from src.views.popup.TagPopup import TagPopup
from src.views.dialogs.mainwindow import MainWindow


'''This file contains the Welcoming Window of the Visualization System.'''
#TODO: Add Sync Option to the Packet View / Synchronize both views together / Create Windows and Linux Installers
class InitialWindow(QMainWindow):
	def __init__(self):
		super(InitialWindow, self).__init__()
		self.setGeometry(500,500,300,300)
		self.resize(800, 600)
		self.setWindowTitle("Data Visualization System")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Data Visualization System")
		self.label.setGeometry(QtCore.QRect(60, 30, 711, 101))
		font = QtGui.QFont()
		font.setPointSize(45)
		self.label.setFont(font)

		self.createNewButton = QtWidgets.QPushButton(self)
		self.createNewButton.setGeometry(QtCore.QRect(310, 330, 141, 32))
		self.createNewButton.setText("Create New Project")

		self.at_start = True

		self.openButton = QtWidgets.QPushButton(self)
		self.openButton.setGeometry(QtCore.QRect(310, 270, 141, 32))
		self.openButton.setText("Open")
		self.openButton.clicked.connect(self.openActionEvent)
		self.openButton.clicked.connect(self.openMainWindowUi)
		self.TagPopup = TagPopup()
		self.MainWindowUi = MainWindow()

	#Instead of openPopup, this will be replaced with the main window.
	def openPopup(self):
		self.TagPopup.show()

	#Instead of openPopup, this will be replaced with the main window.
	def openMainWindowUi(self):
		self.MainWindowUi.show()

	#File manager to open pcap file in wireshark and timeline view
	def openActionEvent(self):
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
					self.file_name = os.path.basename(self.pcap_to_import)
					self.file_name = os.path.splitext(self.file_name)[0]
					self.configname = self.file_name
					if platform.system() == 'Darwin':  # macOS
						subprocess.call(('open', self.pcap_to_import))
					elif platform.system() == 'Windows':  # Windows
						os.startfile(self.pcap_to_import )
					else:  # linux variants
						subprocess.call(('xdg-open', self.pcap_to_import))

def window():
	app = QApplication(sys.argv)
	win = InitialWindow()
	win.show()
	sys.exit(app.exec_())


window()
