# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kick Out Member Poll Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kickMember(object):

    def kickClicked(self):
        #your code here
        self.oldWindow.close()

    def setupUi(self, Dialog):
        self.oldWindow = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 328)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 180, 331, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 50, 161, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 110, 161, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(180, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setObjectName("pushButton_16")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #code
        self.pushButton_16.clicked.connect(self.kickClicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kick out Member Poll"))
        self.label_6.setText(_translate("Dialog", "Reason(s):"))
        self.label_5.setText(_translate("Dialog", "Username to be kicked out"))
        self.label_7.setText(_translate("Dialog", "Name of the group"))
        self.pushButton_16.setText(_translate("Dialog", "Send Poll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_kickMember()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
