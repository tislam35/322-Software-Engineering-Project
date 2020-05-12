# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Invite Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inviteDialog(object):

    def inviteClicked(self):
        #your code here
        self.oldWindow.close()

    def setupUi(self, inviteDialog):
        self.oldWindow = inviteDialog
        inviteDialog.setObjectName("inviteDialog")
        inviteDialog.resize(400, 300)
        self.lineEdit_3 = QtWidgets.QLineEdit(inviteDialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 60, 297, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(inviteDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 27, 297, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(inviteDialog)
        self.label_4.setGeometry(QtCore.QRect(30, 107, 297, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(inviteDialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 140, 301, 61))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(inviteDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(inviteDialog)
        QtCore.QMetaObject.connectSlotsByName(inviteDialog)

        self.pushButton_2.clicked.connect(self.inviteClicked)

    def retranslateUi(self, inviteDialog):
        _translate = QtCore.QCoreApplication.translate
        inviteDialog.setWindowTitle(_translate("inviteDialog", "Invite"))
        self.label_3.setText(_translate("inviteDialog", "Username of Invitee"))
        self.label_4.setText(_translate("inviteDialog", "Message:"))
        self.pushButton_2.setText(_translate("inviteDialog", "Send Invite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inviteDialog = QtWidgets.QDialog()
    ui = Ui_inviteDialog()
    ui.setupUi(inviteDialog)
    inviteDialog.show()
    sys.exit(app.exec_())
