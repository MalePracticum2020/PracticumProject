
import json
import subprocess
import sys
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem, QLabel,QMenu, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import os, webbrowser
from GUI.Dialogs.EditDialog import EditDialog
from PyQt5.QtCore import Qt
from GUI.OpenImage import OpenImage

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
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.editMenu)

    def setTableBasicStructure(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Timed_id", "Start", "ClassName", "Content","Type"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)#(QHeaderView.Stretch)

    def modifyTable(self,stringSearched):
        if not stringSearched == self.stringSearched:
            self.stringSearched = stringSearched
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
                
        except:
            print("Something went wrong while reading TimedScreenshots.JSON")
            self.tableWidget = None


    def buildTableFromSearchInformation(self):
        self.tableWidget.setRowCount(len(self.dataJsonContent))
        row = 0
        for p in self.dataJsonContent:
            if self.stringSearched not in json.dumps(p): 
                self.tableWidget.removeRow(row)
                continue
            else:
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
                newpath = self.folder_path+'/Timed'+ picture[picture.rindex('/'):]
                self.fileList.append(newpath)
                counter = 0
                thumb = Image.open(newpath)
                thumb.thumbnail((150,150))
                thumbPath = newpath.replace('screenshot', 'thumbnail')
                thumbPath.replace('png', 'jpg')
                thumb.save(thumbPath)
                # cell = QPixmap(newpath).scaledToWidth(160).scaledToHeight(160)
                # image = QPixmap(newpath)
                image = QPixmap(thumbPath)
                try:
                    label = QLabel(self)
                    self.resize(image.width(), image.height())
                    label.setPixmap(image)
                    self.tableWidget.setCellWidget(row, 3, label)
                except:
                    cell = QTableWidgetItem(p['content'])
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
            image = OpenImage(path)
        except:
            print('COULD NOT OPEN IMAGE')

    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            with open("internalTime.tmp","w") as outfile:
                outfile.write(currentQTableWidgetItem.text())
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

