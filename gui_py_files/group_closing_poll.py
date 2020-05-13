# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Group Closing Poll.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("TeamMe"))))
from system import *

# from TeamMe.system import *

class Ui_closingGroup(object):

    def votedToClose(self):
        #your code 
        #the attribute under this group - started_close_group 
        #will become true
        system.start_close_group()
        self.oldWindow.close()

    def setupUi(self, Dialog):
        self.oldWindow = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 120, 331, 91))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(140, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setDefault(True)
        self.pushButton_17.setObjectName("pushButton_17")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_17.clicked.connect(self.votedToClose)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Group Closing Poll"))
        self.label_9.setText(_translate("Dialog", "Reason(s):"))
        self.label_8.setText(_translate("Dialog", "Name of the group"))
        self.pushButton_17.setText(_translate("Dialog", "Send Poll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_closingGroup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
