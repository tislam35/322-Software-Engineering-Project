# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log Commits Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_object(object):
    def setupUi(self, object):
        object.setObjectName("object")
        object.resize(268, 195)
        self.label = QtWidgets.QLabel(object)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(object)
        self.dateTimeEdit.setGeometry(QtCore.QRect(40, 50, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_2 = QtWidgets.QLabel(object)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(object)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(object)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 93, 28))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(object)
        QtCore.QMetaObject.connectSlotsByName(object)

    def retranslateUi(self, object):
        _translate = QtCore.QCoreApplication.translate
        object.setWindowTitle(_translate("object", "Log Commits"))
        self.label.setText(_translate("object", "Date of Commits"))
        self.label_2.setText(_translate("object", "Number of Commits"))
        self.pushButton.setText(_translate("object", "Log Commits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    object = QtWidgets.QDialog()
    ui = Ui_object()
    ui.setupUi(object)
    object.show()
    sys.exit(app.exec_())
