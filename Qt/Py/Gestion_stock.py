from PyQt5 import QtCore, QtGui, QtWidgets
from APO_JDEC import Ui_Form2
from add_newrow import Ui_Form
from Drop_row import Ui_Form3

class Ui_Form0(object):
    def openWindow_infos_stock(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_row(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def drop_row(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form0()
        self.ui.setupUi(self.window)
        Form.hide()

    def update(self):
        self.label.adjustSize()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(325, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 300, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda: self.openWindow_infos_stock()) 
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 500, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: self.add_row())
        self.pushButton_2.setGeometry(QtCore.QRect(100, 240, 300, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form, clicked = lambda: self.drop_row())
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 300, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 325, 300, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_5.setGeometry(QtCore.QRect(35, 435, 100, 40))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Gestion de Stock", "Gestion de Stock"))
        self.label.setText(_translate("Form", "Gestion de Stock"))
        self.update()
        self.label_2.setText(_translate("Form", "Veuillez choisir la section voulu :"))
        self.update()
        self.pushButton.setText(_translate("Form", "Consulter les informations des produits en Stock"))
        self.update()
        self.pushButton_2.setText(_translate("Form", "Ajouter un nouveau produit"))
        self.update()
        self.pushButton_3.setText(_translate("Form", "Supprimer un produit"))
        self.update()
        self.pushButton_4.setText(_translate("Form", "Modifier un produit"))
        self.update()
        self.pushButton_5.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form0()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
