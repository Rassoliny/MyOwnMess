# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 291, 81))
        self.label.setObjectName("label")
        self.PasswordPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PasswordPlainTextEdit.setGeometry(QtCore.QRect(180, 287, 311, 71))
        self.PasswordPlainTextEdit.setObjectName("PasswordPlainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 260, 68, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 380, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.LoginPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LoginPlainTextEdit.setGeometry(QtCore.QRect(180, 180, 311, 78))
        self.LoginPlainTextEdit.setObjectName("LoginPlainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ТУТ ЕСТЬ ОЧЕНЬ КЛАССНАЯ КАРТИНКА"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Let\'s Chat!"))

