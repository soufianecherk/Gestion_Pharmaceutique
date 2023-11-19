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
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 800, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.loaddata()
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def loaddata(self):
        import dbf
        table = dbf.Table('Fichier DBF\APO_JDEC.DBF')
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
            item6=str(record[5])

            #print(record)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item2))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item3))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item4))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(item5))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(item6))

            row=row+1
            #print(record.numero , str('|') , record.produit, str('|') , record.quantite , str('|') , record.prix_ppm , str('|') , record.prix_pph , str('|') , record.peremption)
            #print('')
                
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "View Table Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "numero"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "produit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "quantite"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "prix_ppm"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "prix_pph"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "peremption"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
