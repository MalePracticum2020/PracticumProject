from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QCheckBox,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
import json
import sys
class EditDialog(QDialog):

	def __init__(self,cell, file):
		super(EditDialog, self).__init__()
		self.setWindowTitle("Edit Tag")
		self.layout = QVBoxLayout()
		self.line = QLineEdit(self)
		self.layout.addWidget(self.line)
		self.button = QPushButton('Apply', self)
		self.button.move(100,70)
		self.button.clicked.connect(lambda: self.on_click(cell, file))
		self.layout.addWidget(self.button)
		self.setLayout(self.layout)

	def on_click(self,cell, file):
		cell.setText(self.line.text())
		try:
			data = [None]
			with open(file) as json_file:
				data = json.load(json_file)
				str = ''
				if 'auditd_id' in data[0]:
					str = 'auditd_id'
				elif 'keypresses_id' in data[0]:
					str = 'keypresses_id'
				elif 'clicks_id' in data[0]:
					str = 'clicks_id'
				elif 'timed_id' in data[0]:
					str = 'timed_id'
				for key in data:
					if key[str] == cell.row():
						key['content'] = self.line.text()
			with open(file, 'w') as json_file:
				json.dump(data, json_file, indent=4)
		except:
			print('Could not modify parsed data for ', file)
		self.line.setText("")
		self.close()
