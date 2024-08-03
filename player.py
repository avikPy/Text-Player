# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'plyer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QLabel, QPushButton, QTextEdit, QWidget)
from PySide6.QtGui import QFont
import PySide6
import pyttsx3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 341)
        font = PySide6.QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(138, 138, 138);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(243, 239, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    border-color: darkgray;\n"
"}\n"
"QTextEdit {\n"
"    color: rgb(243, 239, 255)\n"
"}")
        self.play_btn = QPushButton(self.centralwidget)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setGeometry(QRect(480, 210, 131, 51))
        self.play_btn.setFont(font)
        self.play_btn.setStyleSheet(u"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 210, 131, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(280, 210, 131, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 80, 531, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        
        self.pushButton_2.clicked.connect(self.DeleteStr)
        self.play_btn.clicked.connect(self.PlayText)
        self.pushButton_3.clicked.connect(self.SaveMp3)
        
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def DeleteStr(self):
        self.textEdit.clear()
    
    def SaveMp3(self):
        text = self.textEdit.toPlainText()
        egin = pyttsx3.init()
        egin.save_to_file(text = text,filename = 'outputPlY.mp3')
        egin.runAndWait()
        
        
            
    def PlayText(self):
        text = self.textEdit.toPlainText()
        egin = pyttsx3.init()
        egin.say(text)
        egin.runAndWait()
        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"player", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0433\u0440\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Player byAvk", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))


