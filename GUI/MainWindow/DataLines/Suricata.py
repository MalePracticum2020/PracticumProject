import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel, QHeaderView,QMenu
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import os
from GUI.Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt
from dateutil.parser import parse
import glob
from datetime import datetime, date, timedelta

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
        self.timeSearched = None
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

    
    def modifyTable(self,stringSearched,timeSearched):
        try:
            if not timeSearched == "":
                incomingTimeSearched = parse(timeSearched)
            else:
                incomingTimeSearched = None
        except Exception as e:
            print(e)
            incomingTimeSearched = None

        if not stringSearched == self.stringSearched or not self.timeSearched == incomingTimeSearched:
            self.stringSearched = stringSearched
            self.timeSearched = incomingTimeSearched
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
            projDir = self.folder_path.split("ProjectData/")
            projName = projDir[1].split("/")[0]
            networkDataxyDir=projDir[0]+"ProjectData/"+projName
            relevDir= glob.glob(networkDataxyDir+'/ecel-export_*')
            self.file = relevDir[0] + '/raw/suricata/eve.json'
            print(self.file)
            with open(self.file) as json_file:
                yolo = []
                for line in json_file:
                    yolo.append(json.loads(line))
                self.dataJsonContent = yolo
                self.buildTableFromSearchInformation()
        except Exception as e:
            print("Something went wrong while reading Suricata.JSON")
            print(e)
            self.tableWidget = None
            
    def buildTableFromSearchInformation(self):
        self.tableWidget.setRowCount(len(self.dataJsonContent))
        row = 0
        for line in self.dataJsonContent:
            line['timestamp'] = line['timestamp'].split('.')[0]
            index = line['timestamp'].index(':')
            hour = int(line['timestamp'][index-2 : index])
            hour = (hour + 5) % 24
            if hour % 10 == 0:
                hour = '0' + str(hour)
            else:
                hour = str(hour)
            time = line['timestamp'][0:index-2] + hour +line['timestamp'][index:]
            if not 'traffic' in line:
                self.tableWidget.removeRow(row)
                continue
            if self.stringSearched not in json.dumps(line):
                self.tableWidget.removeRow(row)
                continue
            else:
                showRow = False
                if self.timeSearched == None:
                    showRow = True
                else:
                    rowTime = parse(str(time))
                    # datetime(year, month, day, hour, minute, second, microsecond)
                    if self.timeSearched.year == rowTime.year and self.timeSearched.month == rowTime.month and self.timeSearched.day == rowTime.day:
                        if self.timeSearched.time().hour == rowTime.time().hour and self.timeSearched.time().minute == rowTime.time().minute:
                            threeSecondsApart = abs(rowTime.time().second - self.timeSearched.time().second)
                            if threeSecondsApart <= 20:
                                showRow = True

                self.suricata_id.append(row)
                cell = QTableWidgetItem(str(row))
                self.tableWidget.setItem(row, 0, cell)

                self.suricata_id.append(time)
                cell = QTableWidgetItem(time)
                self.tableWidget.setItem(row, 1, cell)

                self.start.append(line['traffic']['id'][0])
                cell = QTableWidgetItem(line['traffic']['id'][0])
                self.tableWidget.setItem(row, 2, cell)

                self.classname.append(line['traffic']['label'][0])
                cell = QTableWidgetItem(line['traffic']['label'][0])
                self.tableWidget.setItem(row, 3, cell)

                # self.content.append(p['content'])
                # cell = QTableWidgetItem(p['content'])
                # self.tableWidget.setItem(row, 3, cell)
                # if showRow :

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
            with open("internalTime.tmp","w") as outfile:
                outfile.write(self.tableWidget.item(currentQTableWidgetItem.row(),1).text())#currentQTableWidgetItem.text())
            print(type(currentQTableWidgetItem))
            print("time: " + self.tableWidget.item(currentQTableWidgetItem.row(),1).text())
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
