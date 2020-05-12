# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check Registration Status.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("TeamMe"))))
from system import *
from users import *

from gui_py_files.registration_appeal_dialog import *

class Ui_Dialog(object):

        #your code
    def check_status_clicked(self):
        #collect the email from user input first
        email_to_check=str(self.lineEdit_6.text())
        type_user=""

        #if the object with the email is an OU, then status = approved
        for object in system.OU_list:
            if object.email==email_to_check:
                type_user=="OU"
                msg = QMessageBox()
                msg.setWindowTitle("Approved")
                msg.setText("You have been approved to be an OU.")
                x=msg.exec_()

        #else if the object with the email is a registered visitor, then status = pending
        for tuple in system.registered_visitor_list:
            if tuple[0]==email_to_check:
                type_user=="registered_visitor"
                msg = QMessageBox()
                msg.setWindowTitle("Pending")
                msg.setText("Your registration is pending.")
                x=msg.exec_()

        #else if the object is in blacklist, then status = denied
        for object in system.blacklist:
            if object.email==email_to_check:
                type_user=="blacklist"
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Dialog()
                self.ui.setupUi(self.window)
                self.window.show()    

        #else if object is not in any of those lists, then status = email not found
        if type_user !="OU" and type_user!="registered_visitor" and type_user!="blacklist":
                msg = QMessageBox()
                msg.setWindowTitle("Email not found")
                msg.setText("Your registration email is not found.")
                x=msg.exec_()

        



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 153)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 50, 201, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 27, 137, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 80, 91, 31))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #your code
        #connect pushbutton with action
        self.pushButton_3.clicked.connect(self.check_status_clicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Check Registration Status"))
        self.label_6.setText(_translate("Dialog", "Email"))
        self.pushButton_3.setText(_translate("Dialog", "Check Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
