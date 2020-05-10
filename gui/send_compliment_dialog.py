# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Send Compliment Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from users import *


class Ui_Dialog(object):
    
    #function calling the compliment function
    def complimentClicked(self):
        username = self.lineEdit_2.text()
        message = self.textEdit_2.toPlainText()
        OU.compliment(OU, username, message)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 298)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 140, 331, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 250, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 60, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #connects button to compliment
        self.pushButton_16.clicked.connect(self.complimentClicked)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Send Compliment"))
        self.label_4.setText(_translate("Dialog", "Reason(s):"))
        self.pushButton_16.setText(_translate("Dialog", "Send Compliment"))
        self.label_3.setText(_translate("Dialog", "Username to be complimented"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
