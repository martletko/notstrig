# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interFace2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(876, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.Enter_Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter_Login.setGeometry(QtCore.QRect(50, 60, 191, 22))
        self.Enter_Login.setObjectName(_fromUtf8("Enter_Login"))

        self.Date_And_Time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.Date_And_Time.setGeometry(QtCore.QRect(50, 30, 194, 22))
        self.Date_And_Time.setObjectName(_fromUtf8("Date_And_Time"))

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 821, 571))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        '''
        self.MyProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.MyProgressBar.setGeometry(QtCore.QRect(710, 50, 118, 23))
        self.MyProgressBar.setProperty("value", 24)
        self.MyProgressBar.setObjectName(_fromUtf8("MyProgressBar"))
        '''

        self.Sort_Date = QtWidgets.QPushButton(self.centralwidget)
        self.Sort_Date.setGeometry(QtCore.QRect(270, 20, 93, 28))
        self.Sort_Date.setObjectName(_fromUtf8("Sort_Date"))

        self.Sort_Login = QtWidgets.QPushButton(self.centralwidget)
        self.Sort_Login.setGeometry(QtCore.QRect(270, 60, 93, 28))
        self.Sort_Login.setObjectName(_fromUtf8("Sort_Login"))

        self.Save_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Button.setGeometry(QtCore.QRect(380, 60, 93, 28))
        self.Save_Button.setObjectName(_fromUtf8("Save_Button"))

        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(490, 60, 93, 28))
        self.Clear_Button.setObjectName(_fromUtf8("Clear_Button"))

        self.Print_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Print_Button.setGeometry(QtCore.QRect(600, 60, 93, 28))
        self.Print_Button.setObjectName(_fromUtf8("Print_Button"))

        self.PageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PageLineEdit.setGeometry(QtCore.QRect(710, 60, 40, 22))
        self.PageLineEdit.setObjectName(_fromUtf8("enter_page_Num"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Sort_Date.setText(_translate("MainWindow", "сорт Дата", None))
        self.Sort_Login.setText(_translate("MainWindow", "сорт Логин", None))
        self.Save_Button.setText(_translate("MainWindow", "сохранить", None))
        self.Clear_Button.setText(_translate("MainWindow", "очистить", None))
        self.Print_Button.setText(_translate("MainWindow", "вывести", None))

