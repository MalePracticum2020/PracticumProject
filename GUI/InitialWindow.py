from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QFrame, QStyleFactory,QProxyStyle, QStyle, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit)
import sys
import shutil
import os
import subprocess
import platform
# from helloworld import callme
from pip._internal.utils import logging
import threading
from pip._internal.utils import logging
from GUI.Dialogs.TagPopup import TagPopup
from GUI.MainWindow.MainWindow import MainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

import os
import subprocess

'''This file contains the Welcoming Window of the Visualization System.'''

# TODO: Synchronize the packet view -> timeline view and vice versa


class InitialWindow(QMainWindow):
    def __init__(self):
        super(InitialWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.resize(800, 600)
        self.setWindowTitle("Data Visualization System")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Data Visualization System")
        self.label.setGeometry(QtCore.QRect(150, 30, 711, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)

        self.createNewButton = QtWidgets.QPushButton(self)
        self.createNewButton.setGeometry(QtCore.QRect(310, 330, 141, 32))
        self.createNewButton.setText("Create New Project")
        self.createNewButton.clicked.connect(self.openFileNameDialog)

        self.openButton = QtWidgets.QPushButton(self)
        self.openButton.setGeometry(QtCore.QRect(310, 270, 141, 32))
        self.openButton.setText("Open")
        self.openButton.clicked.connect(self.openFileEvent)
        # self.openButton.clicked.connect(self.openMainWindowUi)
        self.TagPopup = TagPopup()

    # self.MainWindowUi = MainWindow("")
    # Instead of openPopup, this will be replaced with the main window.
    def openPopup(self):
        self.TagPopup.show()

    # Instead of openPopup, this will be replaced with the main window.
    def openMainWindowUi(self):
        self.MainWindowUi.show()

    # File manager to open pcap file in wireshark and timeline view
    def openFileEvent(self):
        pcap_file = QFileDialog()
        filenames, _ = QFileDialog.getOpenFileNames(
            pcap_file, "Select File")

        if len(filenames) < 0:
            logging.debug("File choose cancelled")
            return

        if len(filenames) > 0:
            self.pcap_to_import = filenames[0]
            projDir = self.pcap_to_import.split("ProjectData/")
            projName = projDir[1].split("/")[0]
            projFin=projDir[0]+"ProjectData/"+projName
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', self.pcap_to_import))
            elif platform.system() == 'Windows':  # Windows
                os.startfile(self.pcap_to_import)
            else:  # linux variants
                lua_scripts=[]
                self.dissector_path=projFin+"/GeneratedDissectors/"
                for r, d, f in os.walk(self.dissector_path):
                    for file in f:
                        if '.lua' in file:
                            lua_scripts.append(os.path.join(r, file))
                wirecmd='/usr/local/bin/wireshark -r '+self.pcap_to_import
                if lua_scripts != None and len(lua_scripts) > 0:
                    for lua_script in lua_scripts:
                        wirecmd+= " -Xlua_script:" + lua_script
                
                subprocess.Popen(wirecmd.split())
                # subprocess.call(('xdg-open', self.pcap_to_import))
                    
            file_path = os.path.dirname(os.path.abspath(filenames[0]))
            # file_path = file_path.replace('PCAP', '')
            # file_path=projFin
            print(projFin)
            OGpath = os.path.join(projFin, 'ParsedLogs/OGData')
            if not os.path.exists(OGpath):
                try:
                    os.makedirs(OGpath, exist_ok=True)
                except OSError:
                    print("Creation of the directory failed")
            else:
                print("Directory already exists")
            self.MainWindowUi = MainWindow(projFin)
            self.openMainWindowUi()



    # pid = subprocess.Popen(["python3", "/home/kali/eceld-netsys/PracticumProject/GUI/helloworld.py", self.pcap_to_import])

    def openFileNameDialog(self):
        dialog = QFileDialog()
        projectName, okPressed = QInputDialog.getText(self, "Enter Name of New Project", "This will placed in eceld-netsys/ProjectData folder: ")
        if okPressed and projectName != " ":
            print(projectName, "FIND ME")
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            if folder_path:
                newPath = os.path.dirname(folder_path)+'/'+projectName #creates the new project path with the new project name
                try:
                    shutil.copytree(folder_path, newPath)
                except:
                    print("A folder with this name already exists")
                pcap_file = folder_path + '/PCAP/AnnotatedPCAP.pcapng'
                if platform.system() == 'Darwin':  # macOS
                    subprocess.call(('open', pcap_file))
                elif platform.system() == 'Windows':  # Windows
                    os.startfile(pcap_file)
                else:  # linux variants
                    subprocess.call(('xdg-open', pcap_file))
                self.MainWindowUi = MainWindow(newPath)
                self.openMainWindowUi()


def window():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QtGui.QColor("#0D1225"))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    app.setStyleSheet('QMainWindow{border: 5px solid black;}')
    # error_dialog = QtWidgets.QErrorMessage()
    # error_dialog.showMessage('Oh no!')
	# app.setStyleSheet("background-color: #0D1225;")
	# app.set.setForeground(QtGui.QColor("#F2F2F2"))
    win = InitialWindow()
    win.show()
    sys.exit(app.exec_())


# os.system('python3 .\helloworld.py &') #threading.Thread(target= callme, daemon=True).start()
if os.path.exists("wiretodash.tmp"):
    os.remove("wiretodash.tmp")
if os.path.exists("dashtowire.tmp"):
    os.remove("dashtowire.tmp")
window()

