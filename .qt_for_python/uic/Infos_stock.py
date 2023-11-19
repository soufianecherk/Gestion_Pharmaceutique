# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Infos_stock.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 295)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 80, 75, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 80, 75, 23))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 80, 75, 23))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 80, 75, 23))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 120, 75, 23))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 120, 75, 23))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(220, 120, 75, 23))
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(320, 120, 75, 23))
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 160, 75, 23))
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(120, 160, 75, 23))
        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(220, 160, 75, 23))
        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(320, 160, 75, 23))
        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(20, 200, 75, 23))
        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(120, 200, 75, 23))
        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(220, 200, 75, 23))
        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(320, 200, 75, 23))
        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 260, 75, 23))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 230, 421, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 50, 421, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 341, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Clients", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Facture", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"JACH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"JDAV", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"JDEC", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"JENC", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"JIAC", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"JIAV", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"JIEC", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"JIEN", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"JIRA", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"JIVE", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"JREC", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"JVEN", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"NUME", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"PROD", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"Retour", None))
        self.label.setText(QCoreApplication.translate("Form", u"Consultation des informations des prouits en Stock", None))
    # retranslateUi

