# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assign User Score Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(232, 251)
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 110, 191, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(20, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_50 = QtWidgets.QLabel(Dialog)
        self.label_50.setGeometry(QtCore.QRect(20, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 170, 191, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(20, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton_60 = QtWidgets.QPushButton(Dialog)
        self.pushButton_60.setGeometry(QtCore.QRect(70, 210, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setAutoDefault(False)
        self.pushButton_60.setDefault(True)
        self.pushButton_60.setObjectName("pushButton_60")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Assign User Score"))
        self.label_25.setText(_translate("Dialog", "User to assign"))
        self.label_26.setText(_translate("Dialog", "Score"))
        self.label_50.setText(_translate("Dialog", "User name "))
        self.label_27.setText(_translate("Dialog", "User Type"))
        self.pushButton_60.setText(_translate("Dialog", "Assign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
