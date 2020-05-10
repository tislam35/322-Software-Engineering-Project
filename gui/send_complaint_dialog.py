# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Send Complaint Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from users import *


class Ui_Dialog(object):

    #function that calls complaint
    def complaintClicked(self):
        username = self.lineEdit.text()
        message = self.textEdit.toPlainText()
        OU.complaint(username, message)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 130, 331, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setObjectName("pushButton_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #connecting button to complaint
        self.pushButton_15.clicked.connect(self.complaintClicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Send Compaint"))
        self.label.setText(_translate("Dialog", "Username to be complained with"))
        self.label_2.setText(_translate("Dialog", "Reason(s):"))
        self.pushButton_15.setText(_translate("Dialog", "Send Complaint"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
