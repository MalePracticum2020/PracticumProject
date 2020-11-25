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
			try:
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

			except Exception as e:
				print("Something went wrong on TimeLineDialog")
				print(e)

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
		aa=color.getRgb()
		colormap={"Auditd":"syscal"}
		if color.isValid():
			self.changeObjectBackgroundColor(dataLine['frame'], color)
			self.changeObjectBackgroundColor(dataLine['scrollAreaWidget'], color)
			self.changeObjectBackgroundColor(dataLine['scrollArea'], color)
			self.changeObjectBackgroundColor(dataLine['tableWidget'], color)
			print(aa[0]*257,aa[1]*257,aa[2]*257)
			print(dataLine['name'])
			moddedtext=""
			with open("defaultcolorfilters","r") as colorfile:
				for line in colorfile:
					if colormap[dataLine['name']] in line:
						oldline=line
						oldline=line.split("@")
						temp=oldline[3].split("]")
						# print(temp)
						a=str(aa[0]*257)
						b=str(aa[1]*257)
						c=str(aa[2]*257)
						newcolor = a+","+b+","+c+"]"+temp[1]+"]\n"
						print("@"+oldline[1]+"@"+oldline[2]+"@["+newcolor)
						moddedtext+="@"+oldline[1]+"@"+oldline[2]+"@["+newcolor
					else:
						moddedtext+=line
			with open("defaultcolorfilters","w") as colorfile:
				colorfile.write(moddedtext)
			# fout.close()


	
	def changeObjectBackgroundColor(self, dataLineObject, color):
		p = dataLineObject.palette()
		p.setColor(dataLineObject.backgroundRole(), color)
		dataLineObject.setPalette(p)


