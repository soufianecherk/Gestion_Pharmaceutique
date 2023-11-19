from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 670, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(810, 330, 50, 50))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 100, 133, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(710, 140, 133, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(710, 180, 133, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(710, 220, 133, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(710, 260, 133, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(710, 300, 133, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(710, 335, 90, 35)) #
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.action)
        self.pushButton.setGeometry(QtCore.QRect(710, 380, 133, 50)) #
        self.pushButton.setObjectName("pushButton")
        self.loaddata()
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def update(self):
        self.label.adjustSize() 
            
    def loaddata(self):
        import dbf
        table = dbf.Table('Fichier DBF\APO_JVEN.DBF')
        table.open(dbf.READ_WRITE)
        #table.codepage = dbf.CodePage('cp1252')
        
        row=0
        self.tableWidget.setRowCount(len(table))
        
        for record in table:
            item=str(record[0])
            item2=str(record[1])
            item3=str(record[2])
            item4=str(record[3])
            
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item2))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item3))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item4))

   
            row=row+1
                
    def action(self):
        b = []
        a1 = float(self.lineEdit_2.text())
        a2 = float(self.lineEdit_3.text())
        a3 = float(self.lineEdit_4.text())
        a4 = float(self.lineEdit_5.text())
        a5 = float(self.lineEdit_6.text())
        a6 = float(self.lineEdit_7.text())
        
        if a2 is None :
            a2.Empty()

        b.append(a1)
        b.append(a2)
        b.append(a3)
        b.append(a4)
        b.append(a5)
        b.append(a6)

        s = sum(b)
        self.textBrowser.setText(str(s))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestion Vente"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PRODUIT"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "QUANTITE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "NUMERO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "PRIX_VENTE"))
        self.pushButton.setText(_translate("Form", "Somme"))
        self.lineEdit_2.setText(_translate("Form", "0"))
        self.lineEdit_3.setText(_translate("Form", "0"))
        self.lineEdit_4.setText(_translate("Form", "0"))
        self.lineEdit_5.setText(_translate("Form", "0"))
        self.lineEdit_6.setText(_translate("Form", "0"))
        self.lineEdit_7.setText(_translate("Form", "0"))
        self.label_1.setText(_translate("Form", "DH"))
        self.update()
        self.label.setText(_translate("Form", "Gestion Vente"))
        self.update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
