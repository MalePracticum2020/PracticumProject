
import json
import subprocess
import sys
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem, QLabel,QMenu
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import os, webbrowser
from GUI.Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt
from dateutil.parser import parse
from datetime import datetime, date, timedelta


# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))

class TimedScreenshots(QWidget,):
    folder_path=""
    editDialog = None
    dataJsonContent = None
    
    def __del__(self):
        self.editDialog = None

    def __init__(self,folder_path,stringSearched):
        super(TimedScreenshots, self).__init__()
        self.fileList = []
        self.folder_path = folder_path
        self.stringSearched = stringSearched
        self.timeSearched = None
        self.createTable()


    time_id = []
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
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Timed_id", "Start", "ClassName", "Content","Type"])
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
            self.time_id = []
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
            self.file = self.folder_path+'/ParsedLogs/TimedScreenshots.JSON'
            with open(self.file) as json_file:
                data = json.load(json_file)
                self.dataJsonContent = data
                self.buildTableFromSearchInformation()
                with open(self.folder_path+'/ParsedLogs/OGData/TimedScreenshots.json', "w") as f:
                    json.dump(data, f, indent=4)
        except Exception as e:
            print("Something went wrong while reading MouseClicks.JSON")
            print(e)
            self.tableWidget = None

    ranOnce=False
    def buildTableFromSearchInformation(self):
        self.tableWidget.setRowCount(len(self.dataJsonContent))
        row = 0
        if self.stringSearched:
            self.timeSearched=None
        if self.ranOnce==False:
            self.ranOnce=True
        else:
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        for p in self.dataJsonContent:
            if self.stringSearched and self.stringSearched not in json.dumps(p): 
                self.tableWidget.removeRow(row)
                continue
            else:
                showRow = False
                if self.timeSearched == None:
                    showRow = True
                else:
                    rowTime = parse(str(p['start']))
                    # datetime(year, month, day, hour, minute, second, microsecond)
                    if self.timeSearched.year == rowTime.year and self.timeSearched.month == rowTime.month and self.timeSearched.day == rowTime.day:
                        if self.timeSearched.time().hour == rowTime.time().hour and self.timeSearched.time().minute == rowTime.time().minute:
                            threeSecondsApart = abs(rowTime.time().second - self.timeSearched.time().second)
                            if threeSecondsApart <= 20:
                                showRow = True
                # if showRow :
                self.time_id.append(p['timed_id'])
                cell = QTableWidgetItem(str(p['timed_id']))
                self.tableWidget.setItem(row, 0, cell)

                self.start.append(p['start'])
                cell = QTableWidgetItem(str(p['start']))
                self.tableWidget.setItem(row, 1, cell)

                self.classname.append(p['classname'])
                cell = QTableWidgetItem(p['classname'])
                self.tableWidget.setItem(row, 2, cell)

                self.content.append(p['content'])
                picture = p['content']
                newpath = self.folder_path+'Timed'+ picture[picture.rindex('/'):]
                self.fileList.append(newpath)
                cell = QPixmap(newpath).scaledToWidth(160).scaledToHeight(160)
                try:
                    label = QLabel(self)
                    self.resize(cell.width(), cell.height())
                    label.setPixmap(cell)
                    self.tableWidget.setCellWidget(row, 3, label)
                except:
                    cell = QTableWidgetItem(p['content'])
                    self.tableWidget.setItem(row, 3, cell)
                    print("Problem in timedscreenshots creating cell")

                self.types.append(p['type'])
                cell = QTableWidgetItem(p['type'])
                self.tableWidget.setItem(row, 4, cell)
                if self.stringSearched or self.timeSearched:
                    if showRow:
                        self.tableWidget.selectRow(row)
                # else:
                #     self.tableWidget.removeRow(row)
                #     continue
            row = row +1
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.doubleClicked.connect(self.on_click)

    def editMenu(self, pos):
        row = -1
        column = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row, column = i.row(), i.column()
        if row > -1 and column > -1 and column == 3:
            menu = QMenu()
            item1 = menu.addAction(u'Edit Tag')
            item2 = menu.addAction(u'View Image')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                self.openEditDialog(self.tableWidget.item(row, column))
            elif action == item2:
                self.openViewImage(self.fileList[row])
                print("This is the picture file", self.fileList[row])

    def openViewImage(self, path):
        # img = mpimg.imread(path)
        # plt.imshow(img)
        # try:
        #     img = Image.open(r''+path).show()
        # except IOError:
        #     pass
        try:
            # image = OpenImage(path)
            # img = mpimg.imread(path)
            # plt.imshow(img)
            # plt.show()
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', path))
            elif platform.system() == 'Windows':  # Windows
                os.startfile(path)
            else:
                subprocess.call(['/usr/bin/ristretto', path])
        except:
            print('COULD NOT OPEN IMAGE')

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

