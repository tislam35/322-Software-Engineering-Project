# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Meet Up Poll Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(348, 321)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 70, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(30, 120, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 190, 291, 51))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(110, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setObjectName("pushButton_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Meet Up Poll Dialog"))
        self.label.setText(_translate("Dialog", "Date and Time for the Meet Up"))
        self.label_2.setText(_translate("Dialog", "Start Time"))
        self.label_3.setText(_translate("Dialog", "End Time"))
        self.label_4.setText(_translate("Dialog", "Meeting Summary"))
        self.pushButton_15.setText(_translate("Dialog", "Send Meet Up Poll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
