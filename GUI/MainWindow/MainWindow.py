# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
import sys
from .DataLines.MouseClicks import MouseClicks
from .DataLines.Auditd import Auditd
from .DataLines.Keypresses import Keypresses
from .DataLines.TimedScreenshots import TimedScreenshots
import pandas as pd
import plotly.express as px
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dataLinesSetUp()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 850)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
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
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 234, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(107, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_right_horizontal_layout = QtWidgets.QHBoxLayout()
        self.top_right_horizontal_layout.setObjectName("top_right_horizontal_layout")
        self.sync_button = QtWidgets.QPushButton(self.centralwidget)
        self.sync_button.setStyleSheet("")
        self.sync_button.setObjectName("sync_button")
        self.top_right_horizontal_layout.addWidget(self.sync_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_right_horizontal_layout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.top_right_horizontal_layout.addWidget(self.lineEdit)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.top_right_horizontal_layout.addWidget(self.search_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_right_horizontal_layout.addItem(spacerItem1)
        self.add_data_line = QtWidgets.QPushButton(self.centralwidget)
        self.add_data_line.setObjectName("add_data_line")
        self.top_right_horizontal_layout.addWidget(self.add_data_line)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.top_right_horizontal_layout.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.top_right_horizontal_layout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
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

        #plotly app frame
        self.throughput_frame = QtWebEngineWidgets.QWebEngineView(self)
        self.show_graph()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.throughput_frame.sizePolicy().hasHeightForWidth())
        self.throughput_frame.setSizePolicy(sizePolicy)
        self.throughput_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.throughput_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # self.throughput_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.throughput_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.throughput_frame.setObjectName("throughput_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.throughput_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.throughput_label = QtWidgets.QLabel(self.throughput_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.throughput_label.setFont(font)
        self.throughput_label.setObjectName("throughput_label")
        self.verticalLayout_2.addWidget(self.throughput_label)
        # self.throughput_scrollarea = QtWidgets.QScrollArea(self.throughput_frame)
        # self.throughput_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.throughput_scrollarea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        # self.throughput_scrollarea.setWidgetResizable(True)
        # self.throughput_scrollarea.setObjectName("throughput_scrollarea")
        self.throughput_scrollareawidget = QtWidgets.QWidget()
        self.throughput_scrollareawidget.setGeometry(QtCore.QRect(0, 0, 752, 225))
        self.throughput_scrollareawidget.setObjectName("throughput_scrollareawidget")
        self.gridLayout = QtWidgets.QGridLayout(self.throughput_scrollareawidget)
        self.gridLayout.setObjectName("gridLayout")
        ###
        self.throughput_tablewidget = self.TimedScreenshots.getTable() #self.createTable()
        # self.throughput_tablewidget = QtWidgets.QTableView(self.throughput_scrollareawidget)
        self.throughput_tablewidget.setObjectName("throughput_tablewidget")
        # self.throughput_tablewidget.setColumnCount(0)
        # self.throughput_tablewidget.setRowCount(0)
        ###
        self.gridLayout.addWidget(self.throughput_tablewidget, 0, 0, 1, 1)
        # self.throughput_scrollarea.setWidget(self.throughput_scrollareawidget)
        # self.verticalLayout_2.addWidget(self.throughput_scrollarea)
        self.verticalLayout_6.addWidget(self.throughput_frame)
        self.auditd_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.auditd_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.auditd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.auditd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.auditd_frame.setObjectName("auditd_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.auditd_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.auditd_label = QtWidgets.QLabel(self.auditd_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.auditd_label.setFont(font)
        self.auditd_label.setObjectName("auditd_label")
        self.verticalLayout_3.addWidget(self.auditd_label)
        self.auditd_scrollarea = QtWidgets.QScrollArea(self.auditd_frame)
        self.auditd_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.auditd_scrollarea.setWidgetResizable(True)
        self.auditd_scrollarea.setObjectName("auditd_scrollarea")
        self.auditd_scrollareawidget = QtWidgets.QWidget()
        self.auditd_scrollareawidget.setGeometry(QtCore.QRect(0, 0, 752, 225))
        self.auditd_scrollareawidget.setObjectName("auditd_scrollareawidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.auditd_scrollareawidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #####
        self.auditd_tablewidget = self.Auditd.getTable()
        # self.auditd_tablewidget = QtWidgets.QTableWidget(self.auditd_scrollareawidget)
        self.auditd_tablewidget.setObjectName("auditd_tablewidget")
        # self.auditd_tablewidget.setColumnCount(0)
        # self.auditd_tablewidget.setRowCount(0)
        #####
        self.gridLayout_2.addWidget(self.auditd_tablewidget, 0, 0, 1, 1)
        self.auditd_scrollarea.setWidget(self.auditd_scrollareawidget)
        self.verticalLayout_3.addWidget(self.auditd_scrollarea)
        self.verticalLayout_6.addWidget(self.auditd_frame)
        self.mouseclicks_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.mouseclicks_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.mouseclicks_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mouseclicks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mouseclicks_frame.setObjectName("mouseclicks_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mouseclicks_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mouseclicks_label = QtWidgets.QLabel(self.mouseclicks_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mouseclicks_label.setFont(font)
        self.mouseclicks_label.setObjectName("mouseclicks_label")
        self.verticalLayout_4.addWidget(self.mouseclicks_label)
        self.mouseclicks_scrollarea = QtWidgets.QScrollArea(self.mouseclicks_frame)
        self.mouseclicks_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mouseclicks_scrollarea.setWidgetResizable(True)
        self.mouseclicks_scrollarea.setObjectName("mouseclicks_scrollarea")
        self.mouseclicks_scrollareawidget = QtWidgets.QWidget()
        self.mouseclicks_scrollareawidget.setGeometry(QtCore.QRect(0, 0, 752, 225))
        self.mouseclicks_scrollareawidget.setObjectName("mouseclicks_scrollareawidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mouseclicks_scrollareawidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        #####
        self.mouseclicks_tablewidget = self.MouseClicks.getTable()
        # self.mouseclicks_tablewidget = QtWidgets.QTableWidget(self.mouseclicks_scrollareawidget)
        self.mouseclicks_tablewidget.setObjectName("mouseclicks_tablewidget")
        # self.mouseclicks_tablewidget.setColumnCount(0)
        # self.mouseclicks_tablewidget.setRowCount(0)
        #####
        self.gridLayout_4.addWidget(self.mouseclicks_tablewidget, 0, 0, 1, 1)
        self.mouseclicks_scrollarea.setWidget(self.mouseclicks_scrollareawidget)
        self.verticalLayout_4.addWidget(self.mouseclicks_scrollarea)
        self.verticalLayout_6.addWidget(self.mouseclicks_frame)
        self.keypresses_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.keypresses_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.keypresses_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.keypresses_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypresses_frame.setObjectName("keypresses_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.keypresses_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.keypresses_label = QtWidgets.QLabel(self.keypresses_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.keypresses_label.setFont(font)
        self.keypresses_label.setObjectName("keypresses_label")
        self.verticalLayout_5.addWidget(self.keypresses_label)
        self.keypresses_scrollarea = QtWidgets.QScrollArea(self.keypresses_frame)
        self.keypresses_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.keypresses_scrollarea.setWidgetResizable(True)
        self.keypresses_scrollarea.setObjectName("keypresses_scrollarea")
        self.keypresses_scrollareawidget = QtWidgets.QWidget()
        self.keypresses_scrollareawidget.setGeometry(QtCore.QRect(0, 0, 752, 225))
        self.keypresses_scrollareawidget.setObjectName("keypresses_scrollareawidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.keypresses_scrollareawidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        #####
        self.keypresses_tablewidget = self.Keypresses.getTable()
        # self.keypresses_tablewidget = QtWidgets.QTableWidget(self.keypresses_scrollareawidget)
        self.keypresses_tablewidget.setObjectName("keypresses_tablewidget")
        # self.keypresses_tablewidget.setColumnCount(0)
        # self.keypresses_tablewidget.setRowCount(0)
        #####
        self.gridLayout_5.addWidget(self.keypresses_tablewidget, 0, 0, 1, 1)
        self.keypresses_scrollarea.setWidget(self.keypresses_scrollareawidget)
        self.verticalLayout_5.addWidget(self.keypresses_scrollarea)
        self.verticalLayout_6.addWidget(self.keypresses_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timeline View"))
        self.sync_button.setText(_translate("MainWindow", "Sync"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.add_data_line.setText(_translate("MainWindow", "+ Data Line"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.throughput_label.setText(_translate("MainWindow", "Throughput"))
        self.auditd_label.setText(_translate("MainWindow", "Auditd"))
        self.mouseclicks_label.setText(_translate("MainWindow", "Mouse Clicks"))
        self.keypresses_label.setText(_translate("MainWindow", "Keypresses"))

    def dataLinesSetUp(self):
        self.MouseClicks = MouseClicks()
        self.Auditd = Auditd()
        self.TimedScreenshots = TimedScreenshots()
        self.Keypresses = Keypresses()

    def show_graph(self):
        basePath = os.path.dirname(os.path.abspath(__file__))
        df = pd.read_json(basePath + '/throughput.json')
        fig = px.line(df, x="traffic_xy_id", y="y")
        # fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        self.throughput_frame.setHtml(fig.to_html(include_plotlyjs='cdn'))

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def close_window(self):
        self.close()

