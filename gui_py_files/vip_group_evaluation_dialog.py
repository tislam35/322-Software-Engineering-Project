# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VIP Group Evaluation Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_groupEvaluationDialog(object):
    def setupUi(self, groupEvaluationDialog):
        groupEvaluationDialog.setObjectName("groupEvaluationDialog")
        groupEvaluationDialog.resize(261, 195)
        self.label_2 = QtWidgets.QLabel(groupEvaluationDialog)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(groupEvaluationDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(groupEvaluationDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 90, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(groupEvaluationDialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 93, 28))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(groupEvaluationDialog)
        QtCore.QMetaObject.connectSlotsByName(groupEvaluationDialog)

    def retranslateUi(self, groupEvaluationDialog):
        _translate = QtCore.QCoreApplication.translate
        groupEvaluationDialog.setWindowTitle(_translate("groupEvaluationDialog", "Group Evaluation Scores"))
        self.label_2.setText(_translate("groupEvaluationDialog", "Group ID/Group Name"))
        self.label_3.setText(_translate("groupEvaluationDialog", "Group Score"))
        self.pushButton.setText(_translate("groupEvaluationDialog", "Assign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    groupEvaluationDialog = QtWidgets.QDialog()
    ui = Ui_groupEvaluationDialog()
    ui.setupUi(groupEvaluationDialog)
    groupEvaluationDialog.show()
    sys.exit(app.exec_())
