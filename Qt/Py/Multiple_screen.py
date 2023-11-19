import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from Infos_stock import Ui_Form1
from Gestion_stock import Ui_Form1

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Qt\Py\Gestion_stock.py",self)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("Qt\ui\Infos_stock.ui",self)


#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
screen2=Screen2()
widget.addWidget(MainWindow)
widget.addWidget(screen2)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()




try:
    sys.exit(app.exec_())
except:
    print("Exiting")