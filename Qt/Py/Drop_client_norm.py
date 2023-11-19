from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form9(object):
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
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(590, 20, 113, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda: self.Dropdata())
        self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(720, 20, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 800, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.loaddata()
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def loaddata(self):
        import dbf
        table = dbf.Table('Fichier DBF\CLIENT.DBF')
        table.open(dbf.READ_WRITE)
        #table.codepage = dbf.CodePage('cp1252')
        
        row=0
        self.tableWidget.setRowCount(len(table))
        
        for record in table:
            item=str(record[0])
            item2=str(record[1])
            item3=str(record[2])
            item4=str(record[3])
            item5=str(record[4])
            
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item2))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item3))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item4))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(item5))
            row=row+1

    def Dropdata(self):
        import dbf
        table = dbf.Table('Fichier DBF\CLIENT.DBF')
        table.open(dbf.READ_WRITE)
        nom = int(self.lineEdit.text())
        for record in table:
            if record.CREDIT == nom:
                dbf.delete(record)
                table.pack()
                
    def update(self):
        self.label.adjustSize()            
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Supprimer un client"))
        self.label.setText(_translate("Form", "Supprimer un client"))
        self.update()
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "NOM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ADRESSE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "N. CLIENT"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "CREDIT"))
        self.pushButton.setText(_translate("Form", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form9()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
