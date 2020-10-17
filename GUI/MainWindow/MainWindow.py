# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication,QProxyStyle,QStyle, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox, QHBoxLayout,QSplitter
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
import sys
#from Dash.dash_graph import run_dash
#import helloworld
from .DataLines.MouseClicks import MouseClicks
from .DataLines.Auditd import Auditd
from .DataLines.Keypresses import Keypresses
from .DataLines.TimedScreenshots import TimedScreenshots
import pandas as pd
import plotly.express as px
import os
from PyQt5.QtWebEngineWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import time

class Ui_MainWindow(object):
    dataLineDictionary = {}

    def setupUi(self, MainWindow, folder_path):
        self.dataLinesSetUp(folder_path)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 850)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_right_horizontal_layout = QtWidgets.QHBoxLayout()
        self.top_right_horizontal_layout.setObjectName(
            "top_right_horizontal_layout")
        self.sync_button = QtWidgets.QPushButton(self.centralwidget)
        self.sync_button.setStyleSheet("")
        self.sync_button.setObjectName("sync_button")
        self.top_right_horizontal_layout.addWidget(self.sync_button)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_right_horizontal_layout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.top_right_horizontal_layout.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.top_right_horizontal_layout.addWidget(self.search_button)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_right_horizontal_layout.addItem(spacerItem1)
        # QtWidgets.QPushButton(self.centralwidget)
        self.add_data_line = self.dropDownAddDataLines()
        # self.add_data_line.setObjectName("add_data_line")
        self.top_right_horizontal_layout.addWidget(self.add_data_line)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.top_right_horizontal_layout.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.top_right_horizontal_layout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 1072))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.split_modules = QSplitter(Qt.Vertical)

        # Add Example
        self.createDataLinesDisplayBoxes(folder_path, 0, "Plotly")
        self.createDataLinesDisplayBoxes("", 1, "TimedScreenshots")
        self.createDataLinesDisplayBoxes("", 2, "Auditd")
        self.createDataLinesDisplayBoxes("", 3, "MouseClicks")
        self.createDataLinesDisplayBoxes("", 4, "Keypresses")

        self.save_button.clicked.connect(self.toggle)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @pyqtSlot()
    def toggle(self):
        if self.dataLineDictionary[0]['frame'].isHidden():
            self.dataLineDictionary[0]['frame'].setHidden(False)
        else:
            print(self.dataLineDictionary[0])
            self.dataLineDictionary[0]['frame'].setHidden(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timeline View"))
        self.sync_button.setText(_translate("MainWindow", "Sync"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        # self.add_data_line.setText(_translate("MainWindow", "+ Data Line"))
        self.save_button.setText(_translate("MainWindow", "Save/toggle"))

    def dataLinesSetUp(self, folder_path):
        self.MouseClicks = MouseClicks(folder_path)
        self.Auditd = Auditd(folder_path)
        self.TimedScreenshots = TimedScreenshots(folder_path)
        self.Keypresses = Keypresses(folder_path)

    def dropDownAddDataLines(self):
        cb = CheckableComboBox()
        cb.addItem("/x")
        cb.addItem("/x/x")
        cb.addItems(["/", "/xx", "/ui", "/uy"])
        cb.setEditable(False)
        return cb

    def setWebEngine(self,folder_path):
        # plotly app frame
        self.show_graph(folder_path)
        self.webEngine = QWebEngineView()
        time.sleep(2) #sleep since the dash app is starting up
        self.webEngine.load(QUrl("http://localhost:8050/"))
        self.webEngine.show()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngine.sizePolicy().hasHeightForWidth())
        self.webEngine.setSizePolicy(sizePolicy)
        self.webEngine.setMinimumSize(QtCore.QSize(0, 250))
        self.webEngine.setMaximumSize(QtCore.QSize(16877215, 16877215))
        self.webEngine.setObjectName("web_engine")
        return self.webEngine

    def createDataLinesDisplayBoxes(self, address, itemIndex, type_name):
         # tablewidget
        if type_name == "Plotly":
            frame = self.setWebEngine(address)
            frame.setObjectName("widget" + str(itemIndex))
            # self.verticalLayout_6.addWidget(frame)
            self.split_modules.addWidget(frame)
            self.verticalLayout_6.addWidget(self.split_modules)

            itemDictionaryValue = {
                'frame': frame,
                'scrollArea': "none",
                'scrollAreaWidget': "none",
                'label': "none",
                'gridLayout': "none",
                'verticalLayout': "none",
                'tableWidget': "none"
            }
            self.dataLineDictionary[itemIndex] = itemDictionaryValue
            self.dataLineDictionary[itemIndex]['frame'].setHidden(False)

        else:
            table_flag = False
            if type_name == "Auditd" and self.Auditd.getTable() is not None:
                table_flag = True
                tablewidget = self.Auditd.getTable()
            if type_name == "MouseClicks" and self.MouseClicks.getTable() is not None:
                table_flag = True
                tablewidget = self.MouseClicks.getTable()
            if type_name == "TimedScreenshots" and self.TimedScreenshots.getTable() is not None:
                table_flag = True
                tablewidget = self.TimedScreenshots.getTable()
            if type_name == "Keypresses" and self.Keypresses.getTable() is not None:
                table_flag = True
                tablewidget = self.Keypresses.getTable()
            if table_flag is True:
                tablewidget.setObjectName("widget" + str(itemIndex))
                itemDictionaryValue = self.build_frame(itemIndex,type_name,tablewidget)
                # self.verticalLayout_6.addWidget(itemDictionaryValue['frame'])
                self.split_modules.addWidget(itemDictionaryValue['frame'])
                self.verticalLayout_6.addWidget(self.split_modules)
                # frame.setHidden(True)

    def build_frame(self, itemIndex, type_name, tablewidget):
        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        frame.setMinimumSize(QtCore.QSize(0, 250))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)#frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("auditd_frame" + str(itemIndex))
        verticalLayout = QtWidgets.QVBoxLayout(frame)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout_3" + str(itemIndex))
        label = QtWidgets.QLabel(frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setObjectName("auditd_label" + str(itemIndex))
        verticalLayout.addWidget(label)
        scrollarea = QtWidgets.QScrollArea(frame)
        scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        scrollarea.setWidgetResizable(True)
        scrollarea.setObjectName("auditd_scrollarea" + str(itemIndex))
        scrollareawidget = QtWidgets.QWidget()
        scrollareawidget.setGeometry(QtCore.QRect(0, 0, 752, 225))
        scrollareawidget.setObjectName(
            "auditd_scrollareawidget" + str(itemIndex))
        gridLayout = QtWidgets.QGridLayout(scrollareawidget)
        gridLayout.setObjectName("gridLayout_2" + str(itemIndex))

        gridLayout.addWidget(tablewidget, 0, 0, 1, 1)
        scrollarea.setWidget(scrollareawidget)
        verticalLayout.addWidget(scrollarea)
        _translate = QtCore.QCoreApplication.translate
        label.setText(_translate("MainWindow", type_name))

        itemDictionaryValue = {
            'frame': frame,
            'scrollArea': scrollarea,
            'scrollAreaWidget': scrollareawidget,
            'label': label,
            'gridLayout': gridLayout,
            'verticalLayout': verticalLayout,
            'tableWidget': tablewidget
        }

        self.dataLineDictionary[itemIndex] = itemDictionaryValue
        self.dataLineDictionary[itemIndex]['frame'].setHidden(False)

        return itemDictionaryValue

    def show_graph(self, folder_path):
        #basePath = os.path.dirname(os.path.abspath(__file__))
        basePath = folder_path
        pid = subprocess.Popen(["python3", "/home/kali/eceld-netsys/PracticumProject/GUI/dashrun.py", basePath])
        # with open(basePath +'/ecel-export_1599863833/parsed/tshark/networkDataXY.JSON') as json_file:
        #     data = pd.read_json(json_file)
            # fig = px.line(data, x="traffic_xy_id", y="y")
            # fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
            # self.webEngine.setHtml(fig.to_html(include_plotlyjs='cdn'))
            # threading.Thread(target=run_dash, args=(fig, "Data Visualization"), daemon=True).start()

class CheckableComboBox(QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

    def checkedItems(self):
        checkedItems = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == QtCore.Qt.Checked:
                checkedItems.append(item)
        return checkedItems

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, folder_path):
        super(MainWindow, self).__init__()
        self.setupUi(self, folder_path)
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QtGui.QColor("#002842"))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)

    def close_window(self):
        self.close()
