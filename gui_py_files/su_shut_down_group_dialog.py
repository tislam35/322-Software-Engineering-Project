# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SU Shut Down Group Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shutDownGroupDialog(object):
    def setupUi(self, shutDownGroupDialog):
        shutDownGroupDialog.setObjectName("shutDownGroupDialog")
        shutDownGroupDialog.resize(252, 162)
        self.lineEdit_3 = QtWidgets.QLineEdit(shutDownGroupDialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 50, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(shutDownGroupDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_86 = QtWidgets.QPushButton(shutDownGroupDialog)
        self.pushButton_86.setGeometry(QtCore.QRect(40, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setDefault(True)
        self.pushButton_86.setObjectName("pushButton_86")

        self.retranslateUi(shutDownGroupDialog)
        QtCore.QMetaObject.connectSlotsByName(shutDownGroupDialog)

    def retranslateUi(self, shutDownGroupDialog):
        _translate = QtCore.QCoreApplication.translate
        shutDownGroupDialog.setWindowTitle(_translate("shutDownGroupDialog", "Shut Down Group"))
        self.label_4.setText(_translate("shutDownGroupDialog", "Group Name"))
        self.pushButton_86.setText(_translate("shutDownGroupDialog", "Shut Down Group"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shutDownGroupDialog = QtWidgets.QDialog()
    ui = Ui_shutDownGroupDialog()
    ui.setupUi(shutDownGroupDialog)
    shutDownGroupDialog.show()
    sys.exit(app.exec_())
