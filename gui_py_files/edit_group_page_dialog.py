# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit Group Page Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editGroupDialog(object):
    def setupUi(self, editGroupDialog):
        editGroupDialog.setObjectName("editGroupDialog")
        editGroupDialog.resize(299, 376)
        self.lineEdit = QtWidgets.QLineEdit(editGroupDialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(editGroupDialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(editGroupDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(editGroupDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(editGroupDialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 220, 231, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(editGroupDialog)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 120, 231, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_16 = QtWidgets.QPushButton(editGroupDialog)
        self.pushButton_16.setGeometry(QtCore.QRect(80, 330, 111, 31))
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setObjectName("pushButton_16")

        self.retranslateUi(editGroupDialog)
        QtCore.QMetaObject.connectSlotsByName(editGroupDialog)

    def retranslateUi(self, editGroupDialog):
        _translate = QtCore.QCoreApplication.translate
        editGroupDialog.setWindowTitle(_translate("editGroupDialog", "Edit Group"))
        self.label.setText(_translate("editGroupDialog", "Name of Group"))
        self.label_2.setText(_translate("editGroupDialog", "Programming Languages"))
        self.label_3.setText(_translate("editGroupDialog", "Projects"))
        self.textEdit.setHtml(_translate("editGroupDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("editGroupDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_16.setText(_translate("editGroupDialog", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editGroupDialog = QtWidgets.QDialog()
    ui = Ui_editGroupDialog()
    ui.setupUi(editGroupDialog)
    editGroupDialog.show()
    sys.exit(app.exec_())
