from PyQt5.QtWidgets import QMainWindow
from GUI.InitialWindow import InitialWindow
import sys

if __name__ == '__main__':
    appctxt = QMainWindow(sys.argv)
    gui = InitialWindow()
    gui.setGeometry(200, 200, 300, 300)
    gui.resize(800, 600)
    gui.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)