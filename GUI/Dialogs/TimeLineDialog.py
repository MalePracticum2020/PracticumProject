from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QCheckBox
from PyQt5.QtCore import Qt
import sys
class TimeLineDialog(QDialog):
	checkboxes=[]
	def __init__(self, dataLineDictionary):
		super(TimeLineDialog, self).__init__()
		self.setWindowTitle("Add Data Lines")
		self.layout = QVBoxLayout()
		self.resize(200, 200)
		for i in range(len(dataLineDictionary)):
			self.checkboxes.append(QCheckBox(dataLineDictionary[i]['name'], self))
			if dataLineDictionary[i]['frame'].isHidden():
				self.checkboxes[i].setChecked(False)
			else:
				self.checkboxes[i].setChecked(True)
			self.checkboxes[i].clicked.connect(lambda _,a=i: self.showDataLine(self.checkboxes[a],dataLineDictionary,a))
			self.layout.addWidget(self.checkboxes[i])
		self.setLayout(self.layout)


	def closeEvent(self, event):
		del self.checkboxes[:]

	def showDataLine(self, chechbox, dataLine,i):
		if chechbox.isChecked():
			dataLine[i]['frame'].setHidden(False)
		else:
			dataLine[i]['frame'].setHidden(True)


