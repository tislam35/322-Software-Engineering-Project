# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Browsing Home Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# import form TeamMe GUI class
import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("TeamMe"))))
from Register import *
from Login import *
from more_group_profiles import *
from more_user_profiles import *
from group_page import *
from Profile import *
# from system import *

class Ui_topRatedProfileMain(object):
     # the commented code causes problems after opening a third window
    def registerClicked(self):
        print("METHOD: registerClicked")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterMain()
        self.ui.setupUi(self.window)
        self.window.show()
        print("END: registerClicked")
        return

    def loginClicked(self):
        print("MEHTOD: loginClicked")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, topRatedProfileMain)
        self.window.show()
        return

    def seeMoreGroups(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_moreGroups()
        self.ui.setupUi(self.window)
        self.window.show()

    def seeMoreUsers(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_moreUsers()
        self.ui.setupUi(self.window)
        self.window.show()

    def group1Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_groupWindow()
        self.ui.setupUi(self.window, self.gb1)
        self.window.show()

    def group2Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_groupWindow()
        self.ui.setupUi(self.window, self.gb2)
        self.window.show()

    def group3Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_groupWindow()
        self.ui.setupUi(self.window, self.gb3)
        self.window.show()

    def user1Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profileWindow()
        self.ui.setupUi(self.window, self.ub1)
        self.window.show()

    def user2Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profileWindow()
        self.ui.setupUi(self.window, self.ub2)
        self.window.show()

    def user3Clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profileWindow()
        self.ui.setupUi(self.window, self.ub3)
        self.window.show()

    def setupUi(self, topRatedProfileMain):
        topRatedProfileMain.setObjectName("topRatedProfileMain")
        topRatedProfileMain.resize(795, 584)
        topRatedProfileMain.setAutoFillBackground(False)
        topRatedProfileMain.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(topRatedProfileMain)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonRegister = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRegister.setGeometry(QtCore.QRect(570, 11, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRegister.sizePolicy().hasHeightForWidth())
        self.buttonRegister.setSizePolicy(sizePolicy)
        self.buttonRegister.setMinimumSize(QtCore.QSize(50, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.buttonRegister.setPalette(palette)
        self.buttonRegister.setAutoDefault(False)
        self.buttonRegister.setDefault(True)
        self.buttonRegister.setFlat(False)
        self.buttonRegister.setObjectName("buttonRegister")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 51, 245, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.topUserLabel = QtWidgets.QLabel(self.centralwidget)
        self.topUserLabel.setGeometry(QtCore.QRect(430, 51, 226, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.topUserLabel.setFont(font)
        self.topUserLabel.setObjectName("topUserLabel")
        self.buttonLogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLogin.setGeometry(QtCore.QRect(670, 11, 93, 28))
        self.buttonLogin.setMinimumSize(QtCore.QSize(93, 28))
        self.buttonLogin.setDefault(True)
        self.buttonLogin.setObjectName("buttonLogin")
        self.group1_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.group1_textBrowser.setGeometry(QtCore.QRect(30, 140, 331, 101))
        self.group1_textBrowser.setObjectName("group1_textBrowser")
        self.group2_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.group2_textBrowser.setGeometry(QtCore.QRect(30, 290, 331, 101))
        self.group2_textBrowser.setObjectName("group2_textBrowser")
        self.group3_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.group3_textBrowser.setGeometry(QtCore.QRect(30, 440, 331, 101))
        self.group3_textBrowser.setObjectName("group3_textBrowser")
        self.user1_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.user1_textBrowser.setGeometry(QtCore.QRect(430, 140, 331, 101))
        self.user1_textBrowser.setObjectName("user1_textBrowser")
        self.user2_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.user2_textBrowser.setGeometry(QtCore.QRect(430, 290, 331, 101))
        self.user2_textBrowser.setObjectName("user2_textBrowser")
        self.user3_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.user3_textBrowser.setGeometry(QtCore.QRect(430, 440, 331, 101))
        self.user3_textBrowser.setObjectName("user3_textBrowser")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(394, 121, 16, 429))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.group2_button = QtWidgets.QPushButton(self.centralwidget)
        self.group2_button.setGeometry(QtCore.QRect(20, 260, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.group2_button.setFont(font)
        self.group2_button.setFlat(True)
        self.group2_button.setObjectName("group2_button")
        self.user2_button = QtWidgets.QPushButton(self.centralwidget)
        self.user2_button.setGeometry(QtCore.QRect(420, 260, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user2_button.setFont(font)
        self.user2_button.setFlat(True)
        self.user2_button.setObjectName("user2_button")
        self.group3_button = QtWidgets.QPushButton(self.centralwidget)
        self.group3_button.setGeometry(QtCore.QRect(20, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.group3_button.setFont(font)
        self.group3_button.setFlat(True)
        self.group3_button.setObjectName("group3_button")
        self.user3_button = QtWidgets.QPushButton(self.centralwidget)
        self.user3_button.setGeometry(QtCore.QRect(420, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user3_button.setFont(font)
        self.user3_button.setFlat(True)
        self.user3_button.setObjectName("user3_button")
        self.group1_button = QtWidgets.QPushButton(self.centralwidget)
        self.group1_button.setGeometry(QtCore.QRect(20, 110, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.group1_button.setFont(font)
        self.group1_button.setFlat(True)
        self.group1_button.setObjectName("group1_button")
        self.user1_button = QtWidgets.QPushButton(self.centralwidget)
        self.user1_button.setGeometry(QtCore.QRect(420, 110, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user1_button.setFont(font)
        self.user1_button.setFlat(True)
        self.user1_button.setObjectName("user1_button")
        topRatedProfileMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(topRatedProfileMain)
        self.statusbar.setObjectName("statusbar")
        topRatedProfileMain.setStatusBar(self.statusbar)

        self.retranslateUi(topRatedProfileMain)
        QtCore.QMetaObject.connectSlotsByName(topRatedProfileMain)

        # our code

        top_3 = system.top_3()
        count1 = len(top_3[0])
        count2 = len(top_3[1])
        i1 = 0
        i2 = 0
        if i2 != count2:
            info = str(top_3[1][0].groupName) + "\nGroup Id: " + str(top_3[1][0].groupID) + "\nScore: " + str(
                top_3[1][0].reputation)
            self.group1_textBrowser.setText(info)
            self.group1_button.setEnabled(True)
            self.gb1 = top_3[1][0]
            i2 += 1
            if i2 != count2:
                info = str(top_3[1][1].groupName) + "\nGroup Id: " + str(top_3[1][1].groupID) + "\nScore: " + str(
                    top_3[1][1].reputation)
                self.group2_textBrowser.setText(info)
                self.group2_button.setEnabled(True)
                self.gb2 = top_3[1][1]
                i2 += 1
                if i2 != count2:
                    info = str(top_3[1][2].groupName) + "\nGroup Id: " + str(top_3[1][2].groupID) + "\nScore: " + str(
                        top_3[1][2].reputation)
                    self.group3_textBrowser.setText(info)
                    self.group3_button.setEnabled(True)
                    self.gb3 = top_3[1][2]
        if i1 != count1:
            print(i1)
            print(count1)
            info = str(top_3[0][0].username) + "\nemail: " + str(top_3[0][0].email) + "\nPhone-number: " + str(
                top_3[0][0].phoneNumber) + "\nScore: " + str(top_3[0][0].score)
            self.user1_textBrowser.setText(info)
            self.user1_button.setEnabled(True)
            self.ub1 = top_3[0][0]
            i1 += 1
            if i1 != count1:
                print(i1)
                print(count1)
                info = str(top_3[0][1].username) + "\nemail: " + str(top_3[0][1].email) + "\nPhone-number: " + str(
                    top_3[0][1].phoneNumber) + "\nScore: " + str(top_3[0][1].score)
                self.user2_textBrowser.setText(info)
                self.user2_button.setEnabled(True)
                self.ub2 = top_3[0][1]
                i1 += 1
                if i1 != count1:
                    print(i1)
                    print(count1)
                    info = str(top_3[0][2].username) + "\nemail: " + str(top_3[0][2].email) + "\nPhone-number: " + str(
                        top_3[0][2].phoneNumber) + "\nScore: " + str(top_3[0][2].score)
                    self.user3_textBrowser.setText(info)
                    self.user3_button.setEnabled(True)
                    self.ub3 = top_3[0][2]

        self.buttonRegister.clicked.connect(self.registerClicked)
        self.buttonLogin.clicked.connect(self.loginClicked)
        self.pushButton.clicked.connect(self.seeMoreGroups)
        self.pushButton_2.clicked.connect(self.seeMoreUsers)
        self.group1_button.clicked.connect(self.group1Clicked)
        self.group2_button.clicked.connect(self.group2Clicked)
        self.group3_button.clicked.connect(self.group3Clicked)
        self.user1_button.clicked.connect(self.user1Clicked)
        self.user2_button.clicked.connect(self.user2Clicked)
        self.user3_button.clicked.connect(self.user3Clicked)

        
    def retranslateUi(self, topRatedProfileMain):
        _translate = QtCore.QCoreApplication.translate
        topRatedProfileMain.setWindowTitle(_translate("topRatedProfileMain", "TeamMe Home Browser"))
        self.pushButton.setText(_translate("topRatedProfileMain", "more"))
        self.pushButton_2.setText(_translate("topRatedProfileMain", "more"))
        self.buttonRegister.setText(_translate("topRatedProfileMain", "Register"))
        self.label.setText(_translate("topRatedProfileMain", "Top 3 Group Profiles"))
        self.topUserLabel.setText(_translate("topRatedProfileMain", "Top 3 User Profiles"))
        self.buttonLogin.setText(_translate("topRatedProfileMain", "Login"))
        self.group2_button.setText(_translate("topRatedProfileMain", "Group 2"))
        self.user2_button.setText(_translate("topRatedProfileMain", "User 2"))
        self.group3_button.setText(_translate("topRatedProfileMain", "Group 3"))
        self.user3_button.setText(_translate("topRatedProfileMain", "User 3"))
        self.group1_button.setText(_translate("topRatedProfileMain", "Group 1"))
        self.user1_button.setText(_translate("topRatedProfileMain", "User 1"))
        self.group1_textBrowser.setText("No Group Data Available")
        self.group2_textBrowser.setText("No Group Data Available")
        self.group3_textBrowser.setText("No Group Data Available")
        self.user1_textBrowser.setText("No User Data Available")
        self.user2_textBrowser.setText("No User Data Available")
        self.user3_textBrowser.setText("No User Data Available")
        self.user1_button.setEnabled(False)
        self.user2_button.setEnabled(False)
        self.user3_button.setEnabled(False)
        self.group1_button.setEnabled(False)
        self.group2_button.setEnabled(False)
        self.group3_button.setEnabled(False)
        self.ub1 = None
        self.ub2 = None
        self.ub3 = None
        self.gb1 = None
        self.gb2 = None
        self.gb3 = None
        # topList = system.top_3()
        # topUsers = topList[0]
        # topGroups = topList[1]
        # count = 0
        # for i in topGroups:
        #     gname = i.groupName
        #     gmemb = i.members
        #     gscor = i.reputation
        #     gmembNames = []
        #     for j in gmemb:
        #         gmembNames.append(j.username)
        #     names = ", ".join(gmembNames)
        #     if count == 0:
        #         self.gb1 = i
        #         self.group1_button.setEnabled(True)
        #         self.group1_button.setText(gname)
        #         self.group1_textBrowser.setText("MEMBERS: " + names + "\nSCORE: " + str(gscor))
        #         count += 1
        #     elif count == 1:
        #         self.gb2 = i
        #         self.group2_button.setEnabled(True)
        #         self.group2_button.setText(gname)
        #         self.group2_textBrowser.setText("MEMBERS: " + names + "\nSCORE: " + str(gscor))
        #         count += 1
        #     elif count == 2:
        #         self.gb3 = i
        #         self.group3_button.setEnabled(True)
        #         self.group3_button.setText(gname)
        #         self.group3_textBrowser.setText("MEMBERS: " + names + "\nSCORE: " + str(gscor))
        #         count += 1
        # count = 0
        # for i in topUsers:
        #     uname = i.username
        #     uscor = i.score
        #     if count == 0:
        #         self.ub1 = i
        #         self.user1_button.setEnabled(True)
        #         self.user1_button.setText(uname)
        #         self.user1_textBrowser.setText("SCORE: " + str(uscor))
        #         count += 1
        #     elif count == 1:
        #         self.ub2 = i
        #         self.user2_button.setEnabled(True)
        #         self.user2_button.setText(uname)
        #         self.user2_textBrowser.setText("SCORE: " + str(uscor))
        #         count += 1
        #     elif count == 2:
        #         self.ub3 = i
        #         self.user3_button.setEnabled(True)
        #         self.user3_button.setText(uname)
        #         self.user3_textBrowser.setText("SCORE: " + str(uscor))
        #         count += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    topRatedProfileMain = QtWidgets.QMainWindow()
    ui = Ui_topRatedProfileMain()
    ui.setupUi(topRatedProfileMain)
    topRatedProfileMain.show()
    sys.exit(app.exec_())
