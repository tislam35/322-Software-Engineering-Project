# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time

# import from TeamMe GUI classes
# from TeamMe.gui_py_files.user_home_page import *
from gui_py_files.user_home_page import *
# import from TeamMe classes
# from TeamMe.system import *
from system import *
class Ui_Dialog(object):

    def loginClicked(self):
        print("METHOD: loginClicked")
        msg = QMessageBox()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print("test1")
        bool = system.login(username, password)
        print("test2")
        if bool == False:
            msg.setWindowTitle("Login Failed")
            msg.setText("Login failed, please check your input again.")
            x = msg.exec_()
        else:
            # open and close windows
            self.oldWindow.close()
            self.firstWindow.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_userHomeMain()
            self.ui.setupUi(self.window)
            self.window.show()

    def setupUi(self, Dialog, firstWindow):
        self.oldWindow = Dialog
        self.firstWindow = firstWindow
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 300)
        self.welcomeLabel = QtWidgets.QLabel(Dialog)
        self.welcomeLabel.setGeometry(QtCore.QRect(140, 10, 132, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcomeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 93, 28))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 301, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # your code
        self.pushButton.clicked.connect(self.loginClicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcomeLabel.setText(_translate("Dialog", "WELCOME!"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
