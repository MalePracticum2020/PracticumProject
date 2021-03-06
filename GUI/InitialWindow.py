from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QFrame, QStyleFactory,QProxyStyle, QStyle, QMainWindow, QFileDialog, QMessageBox)
import sys
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
        self.resize(1000, 500)
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
        self.hide()

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
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        if folder_path:
            pcap_file = folder_path + '/PCAP/AnnotatedPCAP.pcapng'
            if platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', pcap_file))
            elif platform.system() == 'Windows':  # Windows
                os.startfile(pcap_file)
            else:  # linux variants
                subprocess.call(('xdg-open', pcap_file))
            self.MainWindowUi = MainWindow(folder_path)
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
if os.path.exists("internalTime.tmp"):
    os.remove("internalTime.tmp")
defaultcolorfilters="""# DO NOT EDIT THIS FILE!  It was created by Wireshark
@timedscreens@timedscreenshots@[65535,21845,65535][65535,65535,65535]
@syscal@systemcalls@[65535,0,0][65535,65535,65535]
@mouseclix@mouseclicks@[0,21845,65535][65535,65535,65535]
@keypress@keypresses@[0,43690,0][65535,65535,65535]
!@suricat@suricata@[21845,65535,65535][0,0,0]
@Bad TCP@tcp.analysis.flags && !tcp.analysis.window_update@[0,0,0][65535,24415,24415]
@HSRP State Change@hsrp.state != 8 && hsrp.state != 16@[0,0,0][65535,63222,0]
@Spanning Tree Topology  Change@stp.type == 0x80@[0,0,0][65535,63222,0]
@OSPF State Change@ospf.msg != 1@[0,0,0][65535,63222,0]
@ICMP errors@icmp.type eq 3 || icmp.type eq 4 || icmp.type eq 5 || icmp.type eq 11 || icmpv6.type eq 1 || icmpv6.type eq 2 || icmpv6.type eq 3 || icmpv6.type eq 4@[0,0,0][0,65535,3598]
@ARP@arp@[54998,59624,65535][0,0,0]
@ICMP@icmp || icmpv6@[49858,49858,65535][0,0,0]
@TCP RST@tcp.flags.reset eq 1@[37008,0,0][65535,63222,32896]
@SCTP ABORT@sctp.chunk_type eq ABORT@[37008,0,0][65535,63222,32896]
@TTL low or unexpected@( ! ip.dst == 224.0.0.0/4 && ip.ttl < 5 && !pim) || (ip.dst == 224.0.0.0/24 && ip.dst != 224.0.0.251 && ip.ttl != 1 && !(vrrp || carp))@[42148,0,0][60652,61680,60395]
@Checksum Errors@cdp.checksum.status=="Bad" || edp.checksum.status=="Bad" || ip.checksum.status=="Bad" || tcp.checksum.status=="Bad" || udp.checksum.status=="Bad"|| sctp.checksum.status=="Bad" || mstp.checksum.status=="Bad"@[0,0,0][65535,24415,24415]
@SMB@smb || nbss || nbns || nbipx || ipxsap || netbios@[65535,64250,39321][0,0,0]
@HTTP@http || tcp.port == 80@[36237,65535,32639][0,0,0]
@IPX@ipx || spx@[65535,58339,58853][0,0,0]
@DCERPC@dcerpc@[51143,38807,65535][0,0,0]
@Routing@hsrp || eigrp || ospf || bgp || cdp || vrrp || carp || gvrp || igmp || ismp@[65535,62451,54998][0,0,0]
@TCP SYN/FIN@tcp.flags & 0x02 || tcp.flags.fin == 1@[41120,41120,41120][0,0,0]
@TCP@tcp@[59367,59110,65535][0,0,0]
@UDP@udp@[28784,57568,65535][0,0,0]
@Broadcast@eth[0] & 1@[65535,65535,65535][32896,32896,32896]
"""
with open("defaultcolorfilters","w") as colorfilters:
    colorfilters.write(defaultcolorfilters)
window()

