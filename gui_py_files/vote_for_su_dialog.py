# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vote for SU Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_voteForSUDialog(object):
    
    def setupUi(self, voteForSUDialog):
        voteForSUDialog.setObjectName("voteForSUDialog")
        voteForSUDialog.resize(296, 181)
        self.label = QtWidgets.QLabel(voteForSUDialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(voteForSUDialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(voteForSUDialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(voteForSUDialog)
        QtCore.QMetaObject.connectSlotsByName(voteForSUDialog)

    def retranslateUi(self, voteForSUDialog):
        _translate = QtCore.QCoreApplication.translate
        voteForSUDialog.setWindowTitle(_translate("voteForSUDialog", "Vote for SU"))
        self.label.setText(_translate("voteForSUDialog", "SU username to be voted"))
        self.pushButton.setText(_translate("voteForSUDialog", "Vote"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voteForSUDialog = QtWidgets.QDialog()
    ui = Ui_voteForSUDialog()
    ui.setupUi(voteForSUDialog)
    voteForSUDialog.show()
    sys.exit(app.exec_())
