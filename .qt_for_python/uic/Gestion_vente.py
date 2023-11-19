# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gestion_vente.ui'
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
        Form.resize(514, 316)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 30, 371, 221))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 180, 101, 23))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 251, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 47, 14))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 151, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 121, 16))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 80, 113, 16))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 140, 113, 16))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 110, 113, 16))
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(280, 45, 42, 21))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 101, 20))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 183, 31, 16))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(270, 172, 41, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 280, 75, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Calculer la somme", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Entrer le nombre de produits acheter par le client :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Enter ID:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Entrer la quantite du produit:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Enter le nom du produit:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Gestion de vente", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"DH", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Retour", None))
    # retranslateUi

