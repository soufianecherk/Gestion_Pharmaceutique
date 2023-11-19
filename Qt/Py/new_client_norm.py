from PyQt5 import QtCore, QtGui, QtWidgets
from APO_JDEC import Ui_Form2 

class Ui_Form11(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 390)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 32, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        #self.lineEdit_2.setGeometry(QtCore.QRect(180, 120, 113, 20))
        #self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 180, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 220, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 260, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 100, 25))
        self.label_2.setObjectName("label_2")
        #self.label_3 = QtWidgets.QLabel(Form)
        #self.label_3.setGeometry(QtCore.QRect(40, 120, 100, 25))
        #self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 100, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 100, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 100, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 100, 25))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.add_row)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(240, 330, 100, 40))
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def add_row(self):
        import dbf
        table = dbf.Table('Fichier DBF/CLIENT.DBF')
        table.open(mode=dbf.READ_WRITE)
        
       # print(self.lineEdit.text())
        NOM = str(self.lineEdit.text())
        EMAIL = str(self.lineEdit_3.text())
        ADRESSE = str(self.lineEdit_4.text())
        NUM_CLIE = int(self.lineEdit_5.text())
        CREDIT = str(self.lineEdit_6.text())

        table.append((NOM, EMAIL, ADRESSE, NUM_CLIE, CREDIT))
        table.close()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form11()
        self.ui.setupUi(self.window)
        Form.hide()
    
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ajouter un nouveau client (N)"))
        self.label.setText(_translate("Form", "Ajouter un nouveau client (N)"))
        self.update()
        self.label_2.setText(_translate("Form", "NOM"))
        self.update()
        self.label_4.setText(_translate("Form", "EMAIL"))
        self.update()
        self.label_5.setText(_translate("Form", "ADRESSE"))
        self.update()
        self.label_6.setText(_translate("Form", "N. CLIENT"))
        #self.update()
        self.label_7.setText(_translate("Form", "CREDIT"))
        self.update()
        self.pushButton.setText(_translate("Form", "Ok"))
        self.update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form11()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
