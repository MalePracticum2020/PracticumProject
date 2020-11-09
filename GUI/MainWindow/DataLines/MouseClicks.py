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
from GUI.Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt

# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))


class MouseClicks(QWidget):
    folder_path=""
    editDialog = None
    dataJsonContent=None

    def __del__(self):
        self.editDialog = None

    def __init__(self,folder_path,stringSearched):
        super(MouseClicks, self).__init__()
        self.folder_path = folder_path
        self.stringSearched = stringSearched
        self.createTable()

    clicks_id = []
    content = []
    types = []
    classname = []
    start = []

    def createTable(self):
       # Create table
        self.setTableBasicStructure()
        self.openJsonFile()
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.editMenu)

    def setTableBasicStructure(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Clicks_id", "Start", "ClassName", "Content","Type"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#(QHeaderView.Stretch)

    def modifyTable(self,stringSearched):
        if not stringSearched == self.stringSearched:
            self.stringSearched = stringSearched
            self.clicks_id = []
            self.content = []
            self.types = []
            self.classname = []
            self.start = []
            # Create table
            self.tableWidget = None
            self.setTableBasicStructure()
            self.buildTableFromSearchInformation()
            self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
            self.tableWidget.customContextMenuRequested.connect(self.editMenu)


    # @cached(cache ={}) 
    def openJsonFile(self):
        try:
            self.file = self.folder_path+'/ParsedLogs/MouseClicks.JSON'
            with open(self.file) as json_file:
                data = json.load(json_file)
                self.dataJsonContent = data
                self.buildTableFromSearchInformation()

        except:
            print("Something went wrong while reading MouseClicks.JSON")
            self.tableWidget = None


    def buildTableFromSearchInformation(self):
        self.tableWidget.setRowCount(len(self.dataJsonContent))
        row = 0
        for p in self.dataJsonContent:
            if self.stringSearched not in json.dumps(p): 
                self.tableWidget.removeRow(row)
                continue
            else:
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

    def editMenu(self, pos):
        row = -1
        column = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row, column = i.row(), i.column()
        if row > -1 and column > -1 and column == 3:
            menu = QMenu()
            item1 = menu.addAction(u'Edit Tag')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                self.openEditDialog(self.tableWidget.item(row, column))

    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(type(currentQTableWidgetItem))
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def openEditDialog(self,cell):
        if self.editDialog == None:
            self.editDialog = EditDialog(cell, self.file)
        if self.editDialog.exec_():
            print("Success!")
        else:
            print("Cancel!")
            del self.editDialog

    def getTable(self):
        return self.tableWidget
