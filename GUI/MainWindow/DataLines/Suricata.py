import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel, QHeaderView,QMenu
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import os
from GUI.Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt

# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))

class Suricata(QWidget):
    folder_path=""
    editDialog = None
    dataJsonContent=None

    def __del__(self):
        self.editDialog = None

    def __init__(self,folder_path,stringSearched):
        super(Suricata, self).__init__()
        self.folder_path = folder_path
        self.stringSearched = stringSearched
        self.createTable()

    suricata_id = []
    content = []
    types = []
    classname = []
    start = []

    def createTable(self):
        # Create table
        self.setTableBasicStructure()
        self.openJsonFile()
        if not self.tableWidget == None:
            try:
                self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
                self.tableWidget.customContextMenuRequested.connect(self.editMenu)
            except Exception as e:
                print(e)

    def setTableBasicStructure(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Suricata_id", "Start", "ClassName", "Content"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#(QHeaderView.Stretch)

    
    def modifyTable(self,stringSearched):
        if not stringSearched == self.stringSearched:
            self.stringSearched = stringSearched
            self.suricata_id  = []
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
            self.file = self.folder_path+'/ParsedLogs/Suricata.JSON' # '/home/kali/PycharmProjects/PracticumProject/GUI/MainWindow/DataLines/ParsedLogs/Suricata.JSON'
            with open(self.file) as json_file:
                data = json.load(json_file)
                self.dataJsonContent = data
                self.buildTableFromSearchInformation()
        except Exception as e:
            print("Something went wrong while reading MouseClicks.JSON")
            print(e)
            self.tableWidget = None
            
    def buildTableFromSearchInformation(self):
        self.tableWidget.setRowCount(len(self.dataJsonContent))
        row = 0
        for p in self.dataJsonContent:
            if self.stringSearched not in json.dumps(p): 
                self.tableWidget.removeRow(row)
                continue
            else:
                self.suricata_id.append(p['suricata_id'])
                cell = QTableWidgetItem(str(p['suricata_id']))
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
