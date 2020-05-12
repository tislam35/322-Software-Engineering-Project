# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assign VIP Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def scoreEntered(self):
        #your code here
        self.oldWindow.close()

    def setupUi(self, Dialog):
        self.oldWindow = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 244)
        self.textBrowser_13 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_13.setGeometry(QtCore.QRect(20, 50, 321, 51))
        self.textBrowser_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(20, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 321, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(130, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setDefault(True)
        self.pushButton_22.setObjectName("pushButton_22")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_22.clicked.connect(self.scoreEntered)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Assign VIP to Group Evaluation"))
        self.textBrowser_13.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">group exit evaluations from group members</span></p></body></html>"))
        self.label_23.setText(_translate("Dialog", "Group name"))
        self.label_24.setText(_translate("Dialog", "VIP to assign"))
        self.pushButton_22.setText(_translate("Dialog", "Assign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
