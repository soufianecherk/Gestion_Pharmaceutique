from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form12(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 400)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 25, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 75, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 115, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 155, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 195, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 235, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 275, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 315, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 75, 100, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 115, 100, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 155, 100, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 195, 100, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 235, 100, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 275, 100, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 315, 100, 25))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda: self.retour())
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(240, 350, 100, 40))
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def add_row(self):
        import dbf
        table = dbf.Table('Fichier DBF/CLIENT_RAMED.DBF')
        table.open(mode=dbf.READ_WRITE)
        
       # print(self.lineEdit.text())
        NOM = str(self.lineEdit.text())
        CIN = str(self.lineEdit_2.text())
        EMAIL = str(self.lineEdit_3.text())
        ADRESSE = str(self.lineEdit_4.text())
        CREDIT = int(self.lineEdit_5.text())
        NORAMED = int(self.lineEdit_6.text())
        PHARMACIEN = str(self.lineEdit_7.text())

        table.append((NOM, CIN, EMAIL, ADRESSE, CREDIT, NORAMED, PHARMACIEN))
        table.close()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form12()
        self.ui.setupUi(self.window)
        Form.hide()
    
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ajouter un nouveau client (R)"))
        self.label.setText(_translate("Form", "Ajouter un nouveau client (R)"))
        self.update()
        self.label_2.setText(_translate("Form", "NOM"))
        self.update()
        self.label_3.setText(_translate("Form", "CIN"))
        self.update()
        self.label_4.setText(_translate("Form", "EMAIL"))
        self.update()
        self.label_5.setText(_translate("Form", "ADRESSE"))
        self.update()
        self.label_6.setText(_translate("Form", "CREDIT"))
        self.update()
        self.label_7.setText(_translate("Form", "NO RAMED"))
        self.update()
        self.label_8.setText(_translate("Form", "PHARAMCIEN"))
        self.update()
        self.pushButton.setText(_translate("Form", "Ok"))
        self.update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form12()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
