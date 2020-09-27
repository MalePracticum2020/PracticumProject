import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
import PyQt5.QtCore as QtCore

class Table(QWidget):

    def __init__(self, jsoncontent):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI(jsoncontent)

    def initUI(self, jsoncontent):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable(jsoncontent)

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self, jsonContent = []):
       # Create table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        if len(jsonContent) > 4:
            self.tableWidget.setRowCount(4)
        else:
            self.tableWidget.setRowCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Time Stamp", "Log", "Tag"])
        self.tableWidget.verticalHeader().setVisible(False)
        row = 0
        for r in jsonContent:
            col = 0
            for item in r:
                if 'image:' in item:
                    cell = QPixmap(item[6:]).scaledToWidth(80)
                    label = QLabel(self)
                    label.setPixmap(cell)
                    self.tableWidget.setCellWidget(row, col, label)
                else:
                    cell = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cell)
                col += 1
            row += 1

        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        print(self.on_click)
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(type(currentQTableWidgetItem))
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table_data = []
    item_1 = ['001', '12:00:11', 'yes']
    item_2 = ['002', '12:01:11', 'image:/home/kali/Downloads/chicken.jpg', 'interesting']
    item_3 = ['003', '12:02:11', 'yes']
    item_4 = ['004', '12:03:11', 'yes']
    table_data.append(item_1)
    table_data.append(item_2)
    table_data.append(item_3)
    table_data.append(item_4)
    ex = Table(table_data)
    sys.exit(app.exec_())
