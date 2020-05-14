# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User Home Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# importing all related gui files



from assign_user_score_dialog import *
from exit_evaluation_dialog import *
from edit_group_page_dialog import *
from su_shut_down_group_dialog import *
from vote_for_su_dialog import *
from vip_group_evaluation_dialog import *
from assign_VIP_dialog import *
from send_compliment_dialog import *
from send_complaint_dialog import *
from meet_up_poll_dialog import *
from more_group_profiles import *
from more_user_profiles import *
from kick_out_member_poll_dialog import *
from group_closing_poll import *
from invite_dialog import *
from reference_dialog import *
from Profile import *
from group_page import *


# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("TeamMe"))))
from system import *
# from TeamMe.system import *

# from TeamMe.system import system


class Ui_userHomeMain(object):


    def referClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReferenceDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    #assigning a vip for group eval
    def VipAssigned(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def complimentClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_compliment()
        self.ui.setupUi(self.window)
        self.window.show()

    def complaintClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_complaint()
        self.ui.setupUi(self.window)
        self.window.show()

    def meetingPoll(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_meetup()
        self.ui.setupUi(self.window)
        self.window.show()

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

    def kickAMember(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_kickMember()
        self.ui.setupUi(self.window)
        self.window.show()

    def closeGroup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_closingGroup()
        self.ui.setupUi(self.window)
        self.window.show()

    def invited(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inviteDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def logout(self):
        self.oldWindow.close()
        system.current_user = None
        system.current_user_group_id = None
        self.firstWindow.show()


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

    def profileEdited(self):
        system.current_user.intro = self.plainTextEdit.toPlainText()
        system.current_user.languages = self.plainTextEdit_3.toPlainText()
        system.current_user.affiliatedGroups = self.plainTextEdit_2.toPlainText()

    def VIPassignScoreClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_groupEvaluationDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def editGroupPageClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_editGroupDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def startEvaluationClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DialogEvaluationExit()
        self.ui.setupUi(self.window)
        self.window.show()

    def shutDownGroupClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_shutDownGroupDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def deductScoresClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DialogAssignScore()
        self.ui.setupUi(self.window)
        self.window.show()

    def voteForSUClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_voteForSUDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def approveCompliment(self):
        if len(system.compliments) > 0:
            try:
                print(system.compliments[0][0])
                system.update_user_score(str(system.compliments[0][0]), 5)
                del system.compliments[0]
            except Exception as e:
                print(e)
                print("bad")
            if len(system.compliments) > 0:
                self.textBrowser_10.setText(str(system.compliments[0][0])  + "\n" + str(system.compliments[0][1]))
            else:
                self.textBrowser_10.setText(" ")

    def rejectComliment(self):
            if len(system.compliments) > 0:
                if system.find_user_by_username(system.compliments[0][0]).complimentsCount % 3 == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle("Complimented 3 times")
                    msg.setText("Must Accept Compliment.")
                    x = msg.exec_()
                    return
                try:
                    print(system.compliments[0][0])
                    del system.compliments[0]
                except:
                    print("bad")
            if len(system.compliments) > 0:
                self.textBrowser_10.setText(str(system.compliments[0][0]) + "\n" + str(system.compliments[0][1]))
            else:
                self.textBrowser_10.setText(" ")

    def approveComplait(self):
        if len(system.complaints) > 0:
            try:
                print(system.complaints[0][0])
                system.update_user_score(str(system.complaints[0][0]), -5)
                del system.complaints[0]
            except Exception as e:
                print(e)
                print("bad")
        if len(system.complaints) > 0:
            self.textBrowser_26.setText(str(system.complaints[0][0]) + "\n" +str(system.complaints[0][1]))
        else:
            self.textBrowser_26.setText(" ")

    def rejectComplait(self):
        if len(system.complaints) > 0:
            try:
                print(system.complaints[0][0])
                del system.complaints[0]
            except:
                print("bad")
        if len(system.complaints) > 0:
            self.textBrowser_26.setText(str(system.complaints[0][0]) + "\n" +str(system.complaints[0][1]))
        else:
            self.textBrowser_26.setText(" ")

    def rejectRegisteredVisitor(self):
        if len(system.registered_visitor_list) > 0:
            system.reject_registered_visitor(system.registered_visitor_list[0])
        else:
            print("bad")
        if len(system.registered_visitor_list) > 0:
            self.textBrowser_7.setText(str(system.registered_visitor_list[0].first_name) + " " + str(system.registered_visitor_list[0].last_name)
                                       + "\nEmail: " + str(system.registered_visitor_list[0].email)
                                       + "\nPhone-number: " + str(system.registered_visitor_list[0].phone_number))
        else:
            self.textBrowser_7.setText(" ")
        print("rejected visitor")

    def approveRegisteredVisitor(self):
        if len(system.registered_visitor_list) > 0:
            system.add_visitor_to_OU(system.registered_visitor_list[0].email)
        if len(system.registered_visitor_list) > 0:
            self.textBrowser_7.setText(str(system.registered_visitor_list[0].first_name) + " " + str(system.registered_visitor_list[0].last_name)
                                       + "\nEmail: " + str(system.registered_visitor_list[0].email) + "\nPhone-number: " + str(system.registered_visitor_list[0].phone_number)
                                       + "\nScore: " + str(system.registered_visitor_list[0].score))
        else:
            self.textBrowser_7.setText(" ")
            print("bad")
        print("approved register visitor")


    def setupUi(self, userHomeMain, temp):

        #changes
        self.oldWindow = userHomeMain
        self.firstWindow = temp

        userHomeMain.setObjectName("userHomeMain")
        userHomeMain.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(userHomeMain)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 571))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.pushButton_3 = QtWidgets.QPushButton(self.homeTab)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 100, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_12 = QtWidgets.QLabel(self.homeTab)
        self.label_12.setGeometry(QtCore.QRect(46, 39, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.layoutWidget_2 = QtWidgets.QWidget(self.homeTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 159, 128, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_4.addWidget(self.label_26)
        self.label_8 = QtWidgets.QLabel(self.homeTab)
        self.label_8.setGeometry(QtCore.QRect(90, 99, 127, 16))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.homeTab)
        self.label_10.setGeometry(QtCore.QRect(120, 129, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.homeTab)
        self.label_4.setGeometry(QtCore.QRect(41, 130, 78, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 80, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.homeTab)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.homeTab)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 60, 341, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.homeTab)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(310, 320, 341, 191))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.homeTab)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(30, 320, 241, 191))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_7 = QtWidgets.QLabel(self.homeTab)
        self.label_7.setGeometry(QtCore.QRect(311, 289, 152, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.homeTab)
        self.label_9.setGeometry(QtCore.QRect(31, 289, 221, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.pushButton_5 = QtWidgets.QPushButton(self.homeTab)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 10, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")


        self.tabWidget.addTab(self.homeTab, "")
        self.browserTab = QtWidgets.QWidget()
        self.browserTab.setObjectName("browserTab")
        self.topUserLabel = QtWidgets.QLabel(self.browserTab)
        self.topUserLabel.setGeometry(QtCore.QRect(420, 21, 226, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.topUserLabel.setFont(font)
        self.topUserLabel.setObjectName("topUserLabel")
        self.group1_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.group1_textBrowser.setGeometry(QtCore.QRect(20, 110, 331, 101))
        self.group1_textBrowser.setObjectName("group1_textBrowser")
        self.user1_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.user1_textBrowser.setGeometry(QtCore.QRect(420, 110, 331, 101))
        self.user1_textBrowser.setObjectName("user1_textBrowser")
        self.label = QtWidgets.QLabel(self.browserTab)
        self.label.setGeometry(QtCore.QRect(21, 21, 245, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.user2_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.user2_textBrowser.setGeometry(QtCore.QRect(420, 260, 331, 101))
        self.user2_textBrowser.setObjectName("user2_textBrowser")
        self.group2_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.group2_textBrowser.setGeometry(QtCore.QRect(20, 260, 331, 101))
        self.group2_textBrowser.setObjectName("group2_textBrowser")
        self.user3_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.user3_textBrowser.setGeometry(QtCore.QRect(420, 410, 331, 101))
        self.user3_textBrowser.setObjectName("user3_textBrowser")
        self.group3_textBrowser = QtWidgets.QTextBrowser(self.browserTab)
        self.group3_textBrowser.setGeometry(QtCore.QRect(20, 410, 331, 101))
        self.group3_textBrowser.setObjectName("group3_textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.browserTab)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_26 = QtWidgets.QPushButton(self.browserTab)
        self.pushButton_26.setGeometry(QtCore.QRect(660, 60, 93, 28))
        self.pushButton_26.setObjectName("pushButton_26")
        self.group1_button = QtWidgets.QPushButton(self.browserTab)
        self.group1_button.setGeometry(QtCore.QRect(10, 80, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group1_button.setFont(font)
        self.group1_button.setFlat(True)
        self.group1_button.setObjectName("group1_button")
        self.group2_button = QtWidgets.QPushButton(self.browserTab)
        self.group2_button.setGeometry(QtCore.QRect(10, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group2_button.setFont(font)
        self.group2_button.setFlat(True)
        self.group2_button.setObjectName("group2_button")
        self.group3_button = QtWidgets.QPushButton(self.browserTab)
        self.group3_button.setGeometry(QtCore.QRect(10, 380, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group3_button.setFont(font)
        self.group3_button.setFlat(True)
        self.group3_button.setObjectName("group3_button")
        self.user2_button = QtWidgets.QPushButton(self.browserTab)
        self.user2_button.setGeometry(QtCore.QRect(410, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user2_button.setFont(font)
        self.user2_button.setFlat(True)
        self.user2_button.setObjectName("user2_button")
        self.user3_button = QtWidgets.QPushButton(self.browserTab)
        self.user3_button.setGeometry(QtCore.QRect(410, 380, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user3_button.setFont(font)
        self.user3_button.setFlat(True)
        self.user3_button.setObjectName("user3_button")
        self.user1_button = QtWidgets.QPushButton(self.browserTab)
        self.user1_button.setGeometry(QtCore.QRect(410, 80, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user1_button.setFont(font)
        self.user1_button.setFlat(True)
        self.user1_button.setObjectName("user1_button")
        self.tabWidget.addTab(self.browserTab, "")
        self.inboxTab = QtWidgets.QWidget()
        self.inboxTab.setObjectName("inboxTab")
        self.label_5 = QtWidgets.QLabel(self.inboxTab)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.inboxTab)
        self.label_11.setGeometry(QtCore.QRect(400, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.inboxTab)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 341, 121))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 230, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.inboxTab)
        self.line.setGeometry(QtCore.QRect(30, 50, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.inboxTab)
        self.line_2.setGeometry(QtCore.QRect(400, 50, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.inboxTab)
        self.textBrowser_5.setGeometry(QtCore.QRect(400, 100, 341, 121))
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_10.setGeometry(QtCore.QRect(400, 230, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 230, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_27 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_27.setGeometry(QtCore.QRect(650, 10, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setDefault(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_52 = QtWidgets.QLabel(self.inboxTab)
        self.label_52.setGeometry(QtCore.QRect(30, 70, 181, 21))
        self.label_52.setObjectName("label_52")
        self.label_54 = QtWidgets.QLabel(self.inboxTab)
        self.label_54.setGeometry(QtCore.QRect(400, 70, 181, 21))
        self.label_54.setObjectName("label_54")
        self.line_11 = QtWidgets.QFrame(self.inboxTab)
        self.line_11.setGeometry(QtCore.QRect(30, 310, 341, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_55 = QtWidgets.QLabel(self.inboxTab)
        self.label_55.setGeometry(QtCore.QRect(30, 330, 211, 21))
        self.label_55.setObjectName("label_55")
        self.pushButton_11 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_11.setGeometry(QtCore.QRect(130, 490, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_24 = QtWidgets.QLabel(self.inboxTab)
        self.label_24.setGeometry(QtCore.QRect(30, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.inboxTab)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 360, 341, 121))
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton_23 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_23.setGeometry(QtCore.QRect(30, 490, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setDefault(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.line_12 = QtWidgets.QFrame(self.inboxTab)
        self.line_12.setGeometry(QtCore.QRect(400, 310, 341, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.inboxTab)
        self.textBrowser_8.setGeometry(QtCore.QRect(400, 360, 341, 121))
        self.textBrowser_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_27 = QtWidgets.QLabel(self.inboxTab)
        self.label_27.setGeometry(QtCore.QRect(400, 270, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton_25 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_25.setGeometry(QtCore.QRect(400, 490, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setDefault(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_28 = QtWidgets.QPushButton(self.inboxTab)
        self.pushButton_28.setGeometry(QtCore.QRect(500, 490, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setDefault(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_56 = QtWidgets.QLabel(self.inboxTab)
        self.label_56.setGeometry(QtCore.QRect(400, 330, 211, 21))
        self.label_56.setObjectName("label_56")
        self.tabWidget.addTab(self.inboxTab, "")
        self.groupManagementTab = QtWidgets.QWidget()
        self.groupManagementTab.setObjectName("groupManagementTab")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_15.setGeometry(QtCore.QRect(250, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.listWidget_6 = QtWidgets.QListWidget(self.groupManagementTab)
        self.listWidget_6.setGeometry(QtCore.QRect(20, 60, 341, 201))
        self.listWidget_6.setObjectName("listWidget_6")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget_6.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_6.addItem(item)
        self.label_14 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_14.setGeometry(QtCore.QRect(20, 10, 233, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_16.setGeometry(QtCore.QRect(20, 270, 111, 31))
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.line_4 = QtWidgets.QFrame(self.groupManagementTab)
        self.line_4.setGeometry(QtCore.QRect(20, 40, 341, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_16 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_16.setGeometry(QtCore.QRect(410, 10, 233, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.line_5 = QtWidgets.QFrame(self.groupManagementTab)
        self.line_5.setGeometry(QtCore.QRect(410, 40, 341, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_17.setGeometry(QtCore.QRect(410, 60, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setDefault(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_18.setGeometry(QtCore.QRect(410, 100, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setDefault(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_21.setGeometry(QtCore.QRect(410, 220, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setDefault(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_17 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_17.setGeometry(QtCore.QRect(20, 340, 233, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.line_6 = QtWidgets.QFrame(self.groupManagementTab)
        self.line_6.setGeometry(QtCore.QRect(20, 370, 341, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_18 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_18.setGeometry(QtCore.QRect(20, 390, 271, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_19.setGeometry(QtCore.QRect(20, 420, 271, 21))
        self.label_19.setObjectName("label_19")
        self.label_28 = QtWidgets.QLabel(self.groupManagementTab)
        self.label_28.setGeometry(QtCore.QRect(400, 330, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.line_13 = QtWidgets.QFrame(self.groupManagementTab)
        self.line_13.setGeometry(QtCore.QRect(400, 370, 341, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_29.setGeometry(QtCore.QRect(400, 390, 161, 31))
        self.pushButton_29.setDefault(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_20.setGeometry(QtCore.QRect(410, 180, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setDefault(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupManagementTab)
        self.pushButton_19.setGeometry(QtCore.QRect(410, 140, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setDefault(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.tabWidget.addTab(self.groupManagementTab, "")
        self.adminSUTab = QtWidgets.QWidget()
        self.adminSUTab.setObjectName("adminSUTab")
        self.line_3 = QtWidgets.QFrame(self.adminSUTab)
        self.line_3.setGeometry(QtCore.QRect(10, 40, 341, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_13 = QtWidgets.QLabel(self.adminSUTab)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_12 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_12.setGeometry(QtCore.QRect(110, 160, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 159, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.line_7 = QtWidgets.QFrame(self.adminSUTab)
        self.line_7.setGeometry(QtCore.QRect(10, 230, 341, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_20 = QtWidgets.QLabel(self.adminSUTab)
        self.label_20.setGeometry(QtCore.QRect(10, 200, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.adminSUTab)
        self.textBrowser_7.setGeometry(QtCore.QRect(10, 90, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.adminSUTab)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 249, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser_10.setFont(font)
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.label_85 = QtWidgets.QLabel(self.adminSUTab)
        self.label_85.setGeometry(QtCore.QRect(10, 60, 241, 21))
        self.label_85.setObjectName("label_85")
        self.pushButton_13 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 330, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_24 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 329, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setDefault(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.adminSUTab)
        self.textBrowser_13.setGeometry(QtCore.QRect(390, 90, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser_13.setFont(font)
        self.textBrowser_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.label_23 = QtWidgets.QLabel(self.adminSUTab)
        self.label_23.setGeometry(QtCore.QRect(390, 60, 181, 21))
        self.label_23.setObjectName("label_23")
        self.line_8 = QtWidgets.QFrame(self.adminSUTab)
        self.line_8.setGeometry(QtCore.QRect(390, 40, 341, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_21 = QtWidgets.QLabel(self.adminSUTab)
        self.label_21.setGeometry(QtCore.QRect(390, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_22.setGeometry(QtCore.QRect(390, 160, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setAutoDefault(True)
        self.pushButton_22.setDefault(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.line_31 = QtWidgets.QFrame(self.adminSUTab)
        self.line_31.setGeometry(QtCore.QRect(390, 270, 341, 16))
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.label_73 = QtWidgets.QLabel(self.adminSUTab)
        self.label_73.setGeometry(QtCore.QRect(390, 230, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.pushButton_85 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_85.setGeometry(QtCore.QRect(390, 320, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setDefault(True)
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_86.setGeometry(QtCore.QRect(390, 290, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setDefault(True)
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_87.setGeometry(QtCore.QRect(110, 500, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setDefault(True)
        self.pushButton_87.setObjectName("pushButton_87")
        self.textBrowser_26 = QtWidgets.QTextBrowser(self.adminSUTab)
        self.textBrowser_26.setGeometry(QtCore.QRect(10, 420, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser_26.setFont(font)
        self.textBrowser_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.line_54 = QtWidgets.QFrame(self.adminSUTab)
        self.line_54.setGeometry(QtCore.QRect(10, 400, 341, 16))
        self.line_54.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_54.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_54.setObjectName("line_54")
        self.label_86 = QtWidgets.QLabel(self.adminSUTab)
        self.label_86.setGeometry(QtCore.QRect(10, 370, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.pushButton_88 = QtWidgets.QPushButton(self.adminSUTab)
        self.pushButton_88.setGeometry(QtCore.QRect(10, 499, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setDefault(True)
        self.pushButton_88.setObjectName("pushButton_88")
        self.tabWidget.addTab(self.adminSUTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line_9 = QtWidgets.QFrame(self.tab)
        self.line_9.setGeometry(QtCore.QRect(30, 50, 341, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_55 = QtWidgets.QPushButton(self.tab)
        self.pushButton_55.setGeometry(QtCore.QRect(30, 200, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setDefault(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.line_21 = QtWidgets.QFrame(self.tab)
        self.line_21.setGeometry(QtCore.QRect(410, 50, 341, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.label_49 = QtWidgets.QLabel(self.tab)
        self.label_49.setGeometry(QtCore.QRect(410, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_16.setGeometry(QtCore.QRect(30, 110, 321, 81))
        self.textBrowser_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_36 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_36.setGeometry(QtCore.QRect(410, 110, 321, 81))
        self.textBrowser_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_36.setObjectName("textBrowser_36")
        self.pushButton_58 = QtWidgets.QPushButton(self.tab)
        self.pushButton_58.setGeometry(QtCore.QRect(410, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setAutoDefault(True)
        self.pushButton_58.setDefault(False)
        self.pushButton_58.setObjectName("pushButton_58")
        self.label_50 = QtWidgets.QLabel(self.tab)
        self.label_50.setGeometry(QtCore.QRect(410, 80, 181, 21))
        self.label_50.setObjectName("label_50")
        self.label_82 = QtWidgets.QLabel(self.tab)
        self.label_82.setGeometry(QtCore.QRect(30, 340, 201, 21))
        self.label_82.setObjectName("label_82")
        self.pushButton_94 = QtWidgets.QPushButton(self.tab)
        self.pushButton_94.setGeometry(QtCore.QRect(30, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setAutoDefault(False)
        self.pushButton_94.setDefault(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.label_81 = QtWidgets.QLabel(self.tab)
        self.label_81.setGeometry(QtCore.QRect(30, 290, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.line_33 = QtWidgets.QFrame(self.tab)
        self.line_33.setGeometry(QtCore.QRect(30, 320, 341, 16))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.label_51 = QtWidgets.QLabel(self.tab)
        self.label_51.setGeometry(QtCore.QRect(30, 80, 181, 21))
        self.label_51.setObjectName("label_51")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(20, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.line_10 = QtWidgets.QFrame(self.tab_2)
        self.line_10.setGeometry(QtCore.QRect(20, 50, 341, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_53 = QtWidgets.QLabel(self.tab_2)
        self.label_53.setGeometry(QtCore.QRect(20, 260, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.line_22 = QtWidgets.QFrame(self.tab_2)
        self.line_22.setGeometry(QtCore.QRect(20, 290, 341, 16))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.tabWidget.addTab(self.tab_2, "")
        userHomeMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(userHomeMain)
        self.statusbar.setObjectName("statusbar")
        userHomeMain.setStatusBar(self.statusbar)

        self.retranslateUi(userHomeMain)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(userHomeMain)

                                #changes
        self.pushButton_27.clicked.connect(self.referClicked)
        self.pushButton_22.clicked.connect(self.VipAssigned)
        self.pushButton_23.clicked.connect(self.VipAssigned)
        self.pushButton_20.clicked.connect(self.complimentClicked)
        self.pushButton_19.clicked.connect(self.complaintClicked)
        self.pushButton_17.clicked.connect(self.meetingPoll)
        self.pushButton_2.clicked.connect(self.seeMoreGroups)
        self.pushButton_26.clicked.connect(self.seeMoreUsers)
        self.pushButton_21.clicked.connect(self.kickAMember)
        self.pushButton_18.clicked.connect(self.closeGroup)
        self.pushButton_16.clicked.connect(self.invited)
        self.pushButton_3.clicked.connect(self.profileEdited)
        self.group1_button.clicked.connect(self.group1Clicked)
        self.group2_button.clicked.connect(self.group2Clicked)
        self.group3_button.clicked.connect(self.group3Clicked)
        self.user1_button.clicked.connect(self.user1Clicked)
        self.user2_button.clicked.connect(self.user2Clicked)
        self.user3_button.clicked.connect(self.user3Clicked)
        self.pushButton_5.clicked.connect(self.logout)


        #more buttons linking
        self.pushButton_55.clicked.connect(self.VIPassignScoreClicked)
        self.pushButton_15.clicked.connect(self.editGroupPageClicked)
        self.pushButton_29.clicked.connect(self.startEvaluationClicked)
        self.pushButton_86.clicked.connect(self.shutDownGroupClicked)
        self.pushButton_85.clicked.connect(self.deductScoresClicked)
        self.pushButton_58.clicked.connect(self.deductScoresClicked)
        self.pushButton_94.clicked.connect(self.voteForSUClicked)

        self.pushButton_24.clicked.connect(self.approveCompliment)
        self.pushButton_13.clicked.connect(self.rejectComliment)
        self.pushButton_88.clicked.connect(self.approveComplait)
        self.pushButton_87.clicked.connect(self.rejectComplait)

        self.pushButton_14.clicked.connect(self.approveRegisteredVisitor)
        self.pushButton_12.clicked.connect(self.rejectRegisteredVisitor)

        #tab 4 -> SU
        #tab 5 -> VIP

        # print("type: "+type(system.current_user).__name__)
        # If current user is an OU, need to hide tab 4 and 5 (admin tabs)
        if type(system.current_user).__name__=="OU":
           self.tabWidget.setTabEnabled(4,False)
           self.tabWidget.setTabEnabled(5,False)
           
        elif type(system.current_user).__name__=="VIP":
            # self.save = self.tabWidget.widget( 4 )
            # self.tabWidget.removeTab(4)
            self.tabWidget.setTabEnabled(4,False)

        else:
        # #     self.setTabEnabled(4,False)
            self.tabWidget.setTabEnabled(5,False)
            # self.save = self.tabWidget.widget( 4 )
            # self.tabWidget.removeTab(5)


        #our code
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

        if len(system.complaints) > 0:
            self.textBrowser_26.setText(str(system.complaints[0][0]) + "\n" + str(system.complaints[0][1]))
        else:
            print("not")

        if len(system.compliments) > 0:
            self.textBrowser_10.setText(str(system.compliments[0][0]) + "\n" + str(system.compliments[0][1]))
        else:
            print("not")

        if len(system.registered_visitor_list) > 0:
            self.textBrowser_7.setText(str(system.registered_visitor_list[0].first_name) + " " + str(system.registered_visitor_list[0].last_name)
                                       + "\nEmail: " + str(system.registered_visitor_list[0].email) + "\nPhone-number: " + str(system.registered_visitor_list[0].phone_number)
                                       + "\nScore: " + str(system.registered_visitor_list[0].score))
        else:
            print("not")

    def retranslateUi(self, userHomeMain):
        _translate = QtCore.QCoreApplication.translate
        userHomeMain.setWindowTitle(_translate("userHomeMain", "User Home Page"))
        self.pushButton_3.setText(_translate("userHomeMain", "Save Changes"))
        self.label_12.setText(_translate("userHomeMain", system.current_user.username))
        self.label_6.setText(_translate("userHomeMain", "Reputation"))
        self.label_26.setText(_translate("userHomeMain", str(system.current_user.score)))
        self.label_8.setText(_translate("userHomeMain", system.current_user.email))
        self.label_10.setText(_translate("userHomeMain", system.current_user.interests))
        self.label_4.setText(_translate("userHomeMain", "Interests: "))
        self.label_2.setText(_translate("userHomeMain", "About Me"))
        self.label_3.setText(_translate("userHomeMain", "Email:"))
        self.plainTextEdit.setPlainText(system.current_user.intro)
        self.plainTextEdit_2.setPlainText(system.current_user.affiliatedGroups)
        self.plainTextEdit_3.setPlainText(system.current_user.languages)
        self.label_7.setText(_translate("userHomeMain", "Groups Affiliation"))
        self.label_9.setText(_translate("userHomeMain", "Programming Languages"))

        self.pushButton_5.setText(_translate("userHomeMain", "Log out"))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("userHomeMain", "Home"))
        self.topUserLabel.setText(_translate("userHomeMain", "Top 3 User Profiles"))
        self.label.setText(_translate("userHomeMain", "Top 3 Group Profiles"))
        self.pushButton_2.setText(_translate("userHomeMain", "more"))
        self.pushButton_26.setText(_translate("userHomeMain", "more"))
        self.group1_button.setText(_translate("userHomeMain", "Group 1"))
        self.group2_button.setText(_translate("userHomeMain", "Group 2"))
        self.group3_button.setText(_translate("userHomeMain", "Group 3"))
        self.user2_button.setText(_translate("userHomeMain", "User 2"))
        self.user3_button.setText(_translate("userHomeMain", "User 3"))
        self.user1_button.setText(_translate("userHomeMain", "User 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.browserTab), _translate("userHomeMain", "Browser"))
        self.label_5.setText(_translate("userHomeMain", "Invitations"))
        self.label_11.setText(_translate("userHomeMain", "Meet Up Poll"))
        self.textBrowser.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Invitation message: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Details include potential projects, other group members, etc.</p></body></html>"))
        self.pushButton.setText(_translate("userHomeMain", " Accept"))
        self.pushButton_4.setText(_translate("userHomeMain", "Reject"))
        self.textBrowser_5.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Meeting time and date</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_10.setText(_translate("userHomeMain", " Accept"))
        self.pushButton_9.setText(_translate("userHomeMain", "Reject"))
        self.pushButton_27.setText(_translate("userHomeMain", "Refer"))
        self.label_52.setText(_translate("userHomeMain", "Invitation 1"))
        self.label_54.setText(_translate("userHomeMain", "Meet up Poll  1"))
        self.label_55.setText(_translate("userHomeMain", "Kick out member username"))
        self.pushButton_11.setText(_translate("userHomeMain", "Reject"))
        self.label_24.setText(_translate("userHomeMain", "Kick out Member Poll"))
        self.textBrowser_6.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reasons to kick out this member</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_23.setText(_translate("userHomeMain", " Accept"))
        self.textBrowser_8.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group Closing reasons</p></body></html>"))
        self.label_27.setText(_translate("userHomeMain", "Group Closing Poll"))
        self.pushButton_25.setText(_translate("userHomeMain", " Accept"))
        self.pushButton_28.setText(_translate("userHomeMain", "Reject"))
        self.label_56.setText(_translate("userHomeMain", "Group Closing Poll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inboxTab), _translate("userHomeMain", "Inbox"))
        self.pushButton_15.setText(_translate("userHomeMain", "Edit Group Page"))
        __sortingEnabled = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        item = self.listWidget_6.item(0)
        item.setText(_translate("userHomeMain", "User Profile A"))
        item = self.listWidget_6.item(1)
        item.setText(_translate("userHomeMain", "     Role, Programming Languages Used, etc."))
        item = self.listWidget_6.item(3)
        item.setText(_translate("userHomeMain", "User Profile B"))
        item = self.listWidget_6.item(4)
        item.setText(_translate("userHomeMain", "     Role, Programming Languages Used, etc."))
        item = self.listWidget_6.item(6)
        item.setText(_translate("userHomeMain", "User Profile C"))
        item = self.listWidget_6.item(7)
        item.setText(_translate("userHomeMain", "     Role, Programming Languages Used, etc."))
        item = self.listWidget_6.item(9)
        item.setText(_translate("userHomeMain", "User Profile D"))
        item = self.listWidget_6.item(10)
        item.setText(_translate("userHomeMain", "     Role, Programming Languages Used, etc."))
        self.listWidget_6.setSortingEnabled(__sortingEnabled)
        self.label_14.setText(_translate("userHomeMain", "Group Members"))
        self.pushButton_16.setText(_translate("userHomeMain", "Invite"))
        self.label_16.setText(_translate("userHomeMain", "Manage Group"))
        self.pushButton_17.setText(_translate("userHomeMain", "Meet Up Poll"))
        self.pushButton_18.setText(_translate("userHomeMain", "Group Closing Poll"))
        self.pushButton_21.setText(_translate("userHomeMain", "Kick Out Member Poll"))
        self.label_17.setText(_translate("userHomeMain", "Meetings"))
        self.label_18.setText(_translate("userHomeMain", "1:00pm - 2:00pm, April 16, 2020."))
        self.label_19.setText(_translate("userHomeMain", "3:00pm - 4:30pm, April 24, 2020."))
        self.label_28.setText(_translate("userHomeMain", "Group Exit Evaluation"))
        self.pushButton_29.setText(_translate("userHomeMain", "Start Evaluation"))
        self.pushButton_20.setText(_translate("userHomeMain", "Write Compliment"))
        self.pushButton_19.setText(_translate("userHomeMain", "Write Complaint"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupManagementTab), _translate("userHomeMain", "Group Management"))
        self.label_13.setText(_translate("userHomeMain", "Account Approval"))
        self.pushButton_12.setText(_translate("userHomeMain", "Reject"))
        self.pushButton_14.setText(_translate("userHomeMain", " Accept"))
        self.label_20.setText(_translate("userHomeMain", "Compliments"))
        self.textBrowser_7.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">referral email and referral score</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Compliment username and details</span></p></body></html>"))
        self.label_85.setText(_translate("userHomeMain", "Account email: Account name"))
        self.pushButton_13.setText(_translate("userHomeMain", "Reject"))
        self.pushButton_24.setText(_translate("userHomeMain", " Accept"))
        self.textBrowser_13.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Exit Reasons</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("userHomeMain", "Group name 1"))
        self.label_21.setText(_translate("userHomeMain", "Assign VIPs to Group Evaluations"))
        self.pushButton_22.setText(_translate("userHomeMain", "Assign"))
        self.label_73.setText(_translate("userHomeMain", "Punishment Actions"))
        self.pushButton_85.setText(_translate("userHomeMain", "Deduct Scores for Group Member"))
        self.pushButton_86.setText(_translate("userHomeMain", "Shut Down Group"))
        self.pushButton_87.setText(_translate("userHomeMain", "Reject"))
        self.textBrowser_26.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Complaints username and details</span></p></body></html>"))
        self.label_86.setText(_translate("userHomeMain", "Complaints"))
        self.pushButton_88.setText(_translate("userHomeMain", " Accept"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adminSUTab), _translate("userHomeMain", "Admin (SU)*"))
        self.label_22.setText(_translate("userHomeMain", "Group Evaluations"))
        self.pushButton_55.setText(_translate("userHomeMain", " Assign Score"))
        self.label_49.setText(_translate("userHomeMain", "User Score Change"))
        self.textBrowser_16.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">group exit evaluations from group members</span></p></body></html>"))
        self.textBrowser_36.setHtml(_translate("userHomeMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Score change reasons</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.pushButton_58.setText(_translate("userHomeMain", "Assign"))
        self.label_50.setText(_translate("userHomeMain", "User name 1"))
        self.label_82.setText(_translate("userHomeMain", "SU name and contact info"))
        self.pushButton_94.setText(_translate("userHomeMain", "Vote for SU"))
        self.label_81.setText(_translate("userHomeMain", "Democratic SU Management"))
        self.label_51.setText(_translate("userHomeMain", "Group name 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("userHomeMain", "Admin (VIP)*"))
        self.label_25.setText(_translate("userHomeMain", "Project Tracker"))
        self.label_53.setText(_translate("userHomeMain", "Project Hierarchy Tree"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("userHomeMain", "Project Management (Creative Feature)"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userHomeMain = QtWidgets.QMainWindow()
    ui = Ui_userHomeMain()
    ui.setupUi(userHomeMain)
    userHomeMain.show()
    sys.exit(app.exec_())
