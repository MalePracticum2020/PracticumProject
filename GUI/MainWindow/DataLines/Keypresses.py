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
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel, QHeaderView,QMenu
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtCore as QtCore
import os
from Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt

# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class Keypresses(QWidget):
    folder_path=""
    editDialog = None

    def __del__(self):
        self.editDialog = None

    def __init__(self,folder_path):
        super(Keypresses, self).__init__()
        self.folder_path = folder_path
        self.createTable()

    keypresses_id = []
    content = []
    types = []
    classname = []
    start = []

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Keypresses_id", "Start", "ClassName", "Content"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#(QHeaderView.Stretch)
        self.openJsonFile()
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.editMenu)

    # @cached(cache ={}) 
    def openJsonFile(self):
        try:
            with open(self.folder_path+'/ParsedLogs/Keypresses.JSON') as json_file:
                data = json.load(json_file)
                self.tableWidget.setRowCount(len(data))
                row = 0
                for p in data:
                    self.keypresses_id.append(p['keypresses_id'])
                    cell = QTableWidgetItem(str(p['keypresses_id']))
                    self.tableWidget.setItem(row, 0, cell)

                    self.start.append(p['start'])
                    cell = QTableWidgetItem(str(p['start']))
                    self.tableWidget.setItem(row, 1, cell)


                    self.content.append(p['content'])
                    cell = QTableWidgetItem(p['content'])
                    self.tableWidget.setItem(row, 2, cell)

                    self.classname.append(p['className'])
                    cell = QTableWidgetItem(p['className'])
                    self.tableWidget.setItem(row, 3, cell)
                    row = row +1
            self.tableWidget.doubleClicked.connect(self.on_click)
        except:
            print("Something went wrong while reading Keypresses.JSON")
            self.tableWidget = None


    def editMenu(self, pos):
        row = -1
        column = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row, column = i.row(), i.column()
        if row > -1 and column > -1:
            menu = QMenu()
            item1 = menu.addAction(u'Edit Tag')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                self.openEditDialog(self.tableWidget.item(row, column))

    @pyqtSlot()
    def on_click(self):
        print(self.on_click)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(type(currentQTableWidgetItem))
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def openEditDialog(self,cell):
        if self.editDialog == None:
            self.editDialog = EditDialog(cell)
        if self.editDialog.exec_():
            print("Success!")
        else:
            print("Cancel!")
            del self.editDialog

    def getTable(self):
        return self.tableWidget