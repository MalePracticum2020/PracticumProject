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
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel, QHeaderView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtCore as QtCore
import os
# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class MouseClicks(QWidget):
    folder_path=""
    def __init__(self,folder_path):
        super(MouseClicks, self).__init__()
        self.folder_path = folder_path
        self.createTable()

    clicks_id = []
    content = []
    types = []
    classname = []
    start = []

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Clicks_id", "Start", "ClassName", "Content","Type"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#(QHeaderView.Stretch)
        self.openJsonFile()

    # @cached(cache ={}) 
    def openJsonFile(self):
        try:
            with open(self.folder_path+'/ParsedLogs/MouseClicks.JSON') as json_file:
                data = json.load(json_file)
                self.tableWidget.setRowCount(len(data))
                row = 0
                for p in data:

                    self.clicks_id.append(p['clicks_id'])
                    cell = QTableWidgetItem(str(p['clicks_id']))
                    self.tableWidget.setItem(row, 0, cell)

                    self.start.append(p['start'])
                    cell = QTableWidgetItem(str(p['start']))
                    self.tableWidget.setItem(row, 1, cell)

                    self.classname.append(p['classname'])
                    cell = QTableWidgetItem(p['classname'])
                    self.tableWidget.setItem(row, 2, cell)

                    self.content.append(p['content'])
                    pixmap = QPixmap("image:"+str(p['content']))
                    if not pixmap.isNull:
                        pixmap.scaledToWidth(80)
                        cell = QLabel(self)
                        cell.setPixmap(pixmap)
                        self.tableWidget.setCellWidget(row, 3, cell)

                        # cell = QPixmap(item[6:]).scaledToWidth(80)
                        # label = QLabel(self)
                        # label.setPixmap(cell)
                        # self.tableWidget.setCellWidget(row, col, label)
                    else:
                        cell = QTableWidgetItem(str(p['content']))
                        self.tableWidget.setItem(row, 3, cell)

                    self.types.append(p['type'])
                    cell = QTableWidgetItem(p['type'])
                    self.tableWidget.setItem(row, 4, cell)
                    row = row +1
            self.tableWidget.doubleClicked.connect(self.on_click)

        except:
            print("Something went wrong while reading MouseClicks.JSON")
            self.tableWidget = None

    @pyqtSlot()
    def on_click(self):
        print(self.on_click)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(type(currentQTableWidgetItem))
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    
    def getTable(self):
        return self.tableWidget