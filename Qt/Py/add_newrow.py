from PyQt5 import QtCore, QtGui, QtWidgets
from APO_JDEC import Ui_Form2 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 390)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 160, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 200, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 240, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 280, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 100, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 100, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 100, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 100, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 100, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 280, 100, 25))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda: self.retour())
        self.pushButton.clicked.connect(self.add_row)
        #self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(240, 330, 100, 40))
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def add_row(self):
        import dbf
        table = dbf.Table('Fichier DBF\APO_JDEC.DBF')
        table.open(mode=dbf.READ_WRITE)
        
        print(self.lineEdit.text())
        numero = int(self.lineEdit.text())
        produit = int(self.lineEdit_2.text())
        quantite = int(self.lineEdit_3.text())
        prix_ppm = float(self.lineEdit_4.text())
        prix_pph = float(self.lineEdit_5.text())
        peremption = self.lineEdit_6.text().split("/")
        table.append((numero, produit, quantite, prix_ppm, prix_pph, dbf.Date(int(peremption[2]), int(peremption[1]),int(peremption[0]))))
        table.close()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        Form.hide()
    
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ajouter un nouveau produit"))
        self.label.setText(_translate("Form", "Ajouter un nouveau produit"))
        self.update()
        self.label_2.setText(_translate("Form", "Numero"))
        self.update()
        self.label_3.setText(_translate("Form", "Produit"))
        self.update()
        self.label_4.setText(_translate("Form", "Quantite"))
        self.update()
        self.label_5.setText(_translate("Form", "Prix_ppm"))
        self.update()
        self.label_6.setText(_translate("Form", "Prix_pph"))
        self.update()
        self.label_7.setText(_translate("Form", "Peremption"))
        self.update()
        self.pushButton.setText(_translate("Form", "Ok"))
        self.update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
