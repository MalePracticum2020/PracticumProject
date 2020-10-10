import plotly
from plotly.graph_objs import Scatter, Layout
import json
import datetime
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from cachetools import cached 
import time 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel,QHeaderView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtCore as QtCore
import os
# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class Auditd(QWidget):
    folder_path=""
    def __init__(self,folder_path):
        super(Auditd, self).__init__()
        self.folder_path = folder_path
        self.createTable()

    auditd_id = []
    content = []
    types = []
    classname = []
    start = []

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Auditd_id", "Start", "ClassName", "Content"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.openJsonFile()
        self.tableWidget.doubleClicked.connect(self.on_click)

    # @cached(cache ={}) 
    def openJsonFile(self):
        with open(self.folder_path+'/ParsedLogs/SystemCalls.JSON') as json_file:
            data = json.load(json_file)
            self.tableWidget.setRowCount(len(data))
            row = 0
            for p in data:

                self.auditd_id.append(p['auditd_id'])
                cell = QTableWidgetItem(str(p['auditd_id']))
                self.tableWidget.setItem(row, 0, cell)

                self.start.append(p['start'])
                cell = QTableWidgetItem(str(p['start']))
                self.tableWidget.setItem(row, 1, cell)

                self.classname.append(p['className'])
                cell = QTableWidgetItem(p['className'])
                self.tableWidget.setItem(row, 2, cell)

                self.content.append(p['content'])
                cell = QTableWidgetItem(p['content'])
                self.tableWidget.setItem(row, 3, cell)

                row = row +1


    @pyqtSlot()
    def on_click(self):
        print(self.on_click)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(type(currentQTableWidgetItem))
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    
    def getTable(self):
        return self.tableWidget