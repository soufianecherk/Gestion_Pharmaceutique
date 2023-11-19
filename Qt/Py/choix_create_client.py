from PyQt5 import QtCore, QtGui, QtWidgets
from new_client_norm import Ui_Form11
from new_client_ramed import Ui_Form12

class Ui_Form8(object):
    def client_norm(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form11()
        self.ui.setupUi(self.window)
        self.window.show()

    def client_ramed(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form12()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form8()
        self.ui.setupUi(self.window)
        Form.hide()

    def update(self):
        self.label.adjustSize()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 90, 160, 30))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form, clicked = lambda: self.client_norm())
        self.pushButton_2.setGeometry(QtCore.QRect(100, 240, 300, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form, clicked = lambda: self.client_ramed())
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 300, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_5.setGeometry(QtCore.QRect(35, 435, 100, 40))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Gestion de Stock", "Ajouter un nouveau client"))
        self.label.setText(_translate("Form", "Veuillez choisir le type du clients: "))
        self.update()
        self.pushButton_2.setText(_translate("Form", "Clients normaux | [+]"))
        self.update()
        self.pushButton_3.setText(_translate("Form", "Clients (Ramed) | [+]"))
        self.update()
        self.pushButton_5.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form8()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
