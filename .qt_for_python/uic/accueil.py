# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accueil.ui'
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
        Form.resize(560, 316)
        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(130, 20, 361, 21))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(210, 80, 161, 151))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 120, 75, 23))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 101, 20))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 80, 161, 151))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 120, 75, 23))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 101, 20))
        self.label.setFont(font1)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(390, 80, 161, 151))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 120, 75, 23))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 101, 20))
        self.label_3.setFont(font1)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 280, 221, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label1.setText(QCoreApplication.translate("Form", u"Application de gestion pharmaceutique GPSV", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Entrer", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Gestion de vente", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Entrer", None))
        self.label.setText(QCoreApplication.translate("Form", u"Gestion de Stock", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Entrer", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Gestion de clients", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Consultation de toute la base de donn\u00e9e", None))
    # retranslateUi

