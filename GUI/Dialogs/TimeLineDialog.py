from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QCheckBox, QHBoxLayout, QColorDialog, QPushButton, QLabel
from PyQt5.QtCore import Qt, pyqtSlot
import sys
class TimeLineDialog(QDialog):
	checkboxes=[]
	def __init__(self, dataLineDictionary):
		super(TimeLineDialog, self).__init__()
		self.setWindowTitle("Add Data Lines")
		self.layout = QVBoxLayout(self)
		self.resize(400, 200)
		title = QLabel( 'xxx' )


		for i in range(len(dataLineDictionary)):
			horizontalLayout = QHBoxLayout()
			self.checkboxes.append(QCheckBox(dataLineDictionary[i]['name'], self))
			if dataLineDictionary[i]['frame'].isHidden():
				self.checkboxes[i].setChecked(False)
			else:
				self.checkboxes[i].setChecked(True)
			self.checkboxes[i].clicked.connect(lambda _,a=i: self.showDataLine(self.checkboxes[a],dataLineDictionary[a]))

			horizontalLayout.addWidget(self.checkboxes[i])
			if not dataLineDictionary[i]['name'] == "Plotly":
				button = QPushButton('Color', self)
				button.setToolTip('Color')
				button.clicked.connect(lambda _,a=i: self.on_click(dataLineDictionary[a]))
				horizontalLayout.addWidget(button)
			self.layout.addLayout(horizontalLayout)

		self.setLayout(self.layout)

	def closeEvent(self, event):
		del self.checkboxes[:]

	def showDataLine(self, chechbox, dataLine):
		if chechbox.isChecked():
			dataLine['frame'].setHidden(False)
		else:
			dataLine['frame'].setHidden(True)
	
	@pyqtSlot()
	def on_click(self, dataLine):
		self.openColorDialog(dataLine)
	
	def openColorDialog(self,dataLine):
		color = QColorDialog.getColor()
		if color.isValid():
			self.changeObjectBackgroundColor(dataLine['frame'], color)
			self.changeObjectBackgroundColor(dataLine['scrollAreaWidget'], color)
			self.changeObjectBackgroundColor(dataLine['scrollArea'], color)
			self.changeObjectBackgroundColor(dataLine['tableWidget'], color)
	
	def changeObjectBackgroundColor(self, dataLineObject, color):
		p = dataLineObject.palette()
		p.setColor(dataLineObject.backgroundRole(), color)
		dataLineObject.setPalette(p)


