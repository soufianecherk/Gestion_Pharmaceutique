from PyQt5 import QtCore, QtGui, QtWidgets
from accueil import Ui_Form


class Ui_Form20(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 380)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(65, 40, 340, 320))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow_accueil())
        self.pushButton.clicked.connect(Form.close)
        self.pushButton.setGeometry(QtCore.QRect(180, 260, 80, 40))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 113, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 160, 113, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(5, 100, 100, 26))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(5, 160, 100, 26))
        self.label_3.setObjectName("label_3")

    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.loginfunction)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        import dbf
        table = dbf.Table('Fichier DBF\login.DBF')
        table.open(dbf.READ_ONLY)
        email=self.lineEdit.text()
        password=self.lineEdit_2.text()
        for record in table:
            if record.EMAIL == email and record.PASSWORD == password:
                open.openWindow_accueil()

    def openWindow_accueil(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def update(self):
        self.label.adjustSize()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "Login"))
        self.update()
        self.label_2.setText(_translate("Form", "Username"))
        self.update()
        self.label_3.setText(_translate("Form", "Password"))
        self.update()
        self.pushButton.setText(_translate("Form", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form20()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
