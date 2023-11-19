from tkinter import Widget
from PyQt5 import QtCore, QtGui, QtWidgets
from Gestion_stock import Ui_Form0
from Gestion_vente import Ui_Form2
from Gestion_client import Ui_Form4
from Infos_stock import Ui_Form1

class Ui_Form(object):
    def openWindow_Gestion_stock(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form0()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow_Gestion_vente(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow_gestion_clients(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form4()
        self.ui.setupUi(self.window)
        self.window.show()  
    
    #def openWindow_infos_BD(self):
    #    self.window = QtWidgets.QWidget()
    #    self.ui = Ui_Form1()
    #    self.ui.setupUi(self.window)
    #    self.window.show()       
    
    def update(self):
        self.label.adjustSize()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(175, 40, 550, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(295, 150, 250, 250)) #
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow_Gestion_vente())
        self.pushButton_3.setGeometry(QtCore.QRect(25, 150, 200, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 150, 250, 250)) #
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow_Gestion_stock())
        self.pushButton.setGeometry(QtCore.QRect(25, 150, 200, 50))
        self.pushButton.setObjectName("pushButton")
        #
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(570, 150, 250, 250))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.openWindow_gestion_clients())
        self.pushButton_4.setGeometry(QtCore.QRect(25, 150, 200, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: self.openWindow_infos_BD()) 
        #self.pushButton_2.setGeometry(QtCore.QRect(400, 430, 400, 50))
        #self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 45, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Application de gestion pharmaceutique | GPSV"))
        self.label1.setText(_translate("Form", "Application de gestion pharmaceutique | GPSV"))
        self.update()
        self.pushButton_3.setText(_translate("Form", "Entrer"))
        self.update()
        self.label_2.setText(_translate("Form", "Gestion de vente"))
        self.update()
        self.pushButton.setText(_translate("Form", "Entrer"))
        self.update()
        self.label_3.setText(_translate("Form", "Gestion de client"))
        self.update()
        self.pushButton_4.setText(_translate("Form", "Entrer"))
        self.update()
        #self.pushButton_2.setText(_translate("Form", "Consultation de toute la base de donnée"))
        #self.update()
        self.label.setText(_translate("Form", "Gestion de Stock"))
        self.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
