from PyQt5 import QtCore, QtGui, QtWidgets
from choix_client import Ui_Form5
from choix_create_client import Ui_Form8
from choix_drop_client import Ui_Form10

class Ui_Form4(object):
    def openWindow_infos_client(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form5()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_client(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form8()
        self.ui.setupUi(self.window)
        self.window.show()

    def drop_client(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form10()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form4()
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
        self.pushButton = QtWidgets.QPushButton(Form, clicked = lambda: self.openWindow_infos_client()) 
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 500, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: self.add_client())
        self.pushButton_2.setGeometry(QtCore.QRect(100, 240, 300, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form, clicked = lambda: self.drop_client())
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
        Form.setWindowTitle(_translate("Gestion de Stock", "Gestion de clients"))
        self.label.setText(_translate("Form", "Gestion de clients"))
        self.update()
        self.label_2.setText(_translate("Form", "Veuillez choisir la section voulu :"))
        self.update()
        self.pushButton.setText(_translate("Form", "Consulter les informations des clients"))
        self.update()
        self.pushButton_2.setText(_translate("Form", "Ajouter un nouveau clients"))
        self.update()
        self.pushButton_3.setText(_translate("Form", "Supprimer un client"))
        self.update()
        self.pushButton_4.setText(_translate("Form", "Modifier un client"))
        self.update()
        self.pushButton_5.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form4()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
