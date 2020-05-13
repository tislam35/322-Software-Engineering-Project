# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reference Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReferenceDialog(object):
    def setupUi(self, ReferenceDialog):
        ReferenceDialog.setObjectName("ReferenceDialog")
        ReferenceDialog.resize(289, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReferenceDialog.sizePolicy().hasHeightForWidth())
        ReferenceDialog.setSizePolicy(sizePolicy)
        self.refer_pushButton = QtWidgets.QPushButton(ReferenceDialog)
        self.refer_pushButton.setGeometry(QtCore.QRect(90, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.refer_pushButton.setFont(font)
        self.refer_pushButton.setObjectName("refer_pushButton")
        self.lineEdit = QtWidgets.QLineEdit(ReferenceDialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 80, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(ReferenceDialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ReferenceDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(ReferenceDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 150, 181, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(ReferenceDialog)
        QtCore.QMetaObject.connectSlotsByName(ReferenceDialog)

    def retranslateUi(self, ReferenceDialog):
        _translate = QtCore.QCoreApplication.translate
        ReferenceDialog.setWindowTitle(_translate("ReferenceDialog", "Reference Info"))
        self.refer_pushButton.setText(_translate("ReferenceDialog", "Refer"))
        self.label.setText(_translate("ReferenceDialog", "Visitor Email"))
        self.label_2.setText(_translate("ReferenceDialog", "Score to assign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReferenceDialog = QtWidgets.QDialog()
    ui = Ui_ReferenceDialog()
    ui.setupUi(ReferenceDialog)
    ReferenceDialog.show()
    sys.exit(app.exec_())
