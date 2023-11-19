# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gestion_stock.ui'
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 121, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 181, 16))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 90, 321, 41))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 160, 151, 31))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 160, 151, 31))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 210, 161, 31))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 260, 75, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Gestion de Stock", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Veuillez choisir la section voulu :", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Consulter les informations des produits en Stock", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Ajouter un nouveau produit", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Supprimer un produit", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Modifier un produit", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Retour", None))
    # retranslateUi

