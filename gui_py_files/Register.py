# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# import from TeamMe classes
from TeamMe.system import *

class Ui_RegisterMain(object):

    def setupUi(self, RegisterMain):
        RegisterMain.setObjectName("RegisterMain")
        RegisterMain.resize(364, 558)
        self.centralwidget = QtWidgets.QWidget(RegisterMain)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 306, 392))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(121, 61))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_3.addWidget(self.lineEdit_9, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 2, 0, 1, 1)
        RegisterMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterMain)
        self.statusbar.setObjectName("statusbar")
        RegisterMain.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterMain)
        QtCore.QMetaObject.connectSlotsByName(RegisterMain)


        #connect the push button with conditional pop up windows
        self.pushButton.clicked.connect(self.show_popup)

    def retranslateUi(self, RegisterMain):
        _translate = QtCore.QCoreApplication.translate
        RegisterMain.setWindowTitle(_translate("RegisterMain", "Register"))
        self.label_8.setText(_translate("RegisterMain", "Reference Username"))
        self.label_5.setText(_translate("RegisterMain", "Interests"))
        self.label.setText(_translate("RegisterMain", "Name"))
        self.label_3.setText(_translate("RegisterMain", "Phone Number"))
        self.label_2.setText(_translate("RegisterMain", "Email"))
        self.lineEdit_4.setText(_translate("RegisterMain", "Area code"))
        self.lineEdit_2.setText(_translate("RegisterMain", "Last"))
        self.label_4.setText(_translate("RegisterMain", "-"))
        self.lineEdit.setText(_translate("RegisterMain", "First"))
        self.pushButton.setText(_translate("RegisterMain", "Register"))

    def show_popup(self):
        msg = QMessageBox()

        msg.setWindowTitle("Register Failed")
        msg.setText("Register Failed, please check your input again.")
        x=msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterMain = QtWidgets.QMainWindow()
    ui = Ui_RegisterMain()
    ui.setupUi(RegisterMain)
    RegisterMain.show()
    sys.exit(app.exec_())
