#!/usr/bin/python
'''
PICK Tool: Team6 - Team404

Program Purpose:
        - Prototype of the GUI for the clients

Date:
        - February 2020

Dependencies:
        - pyqt5

NOTES:

'''

import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui

class Ui_Dialog(object):
    def openWindowteam(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_team()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_event()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def openWindowload(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Loadprject()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.pushButton_2start = QtWidgets.QPushButton(Dialog)
        self.pushButton_2start.setGeometry(QtCore.QRect(720, 310, 401, 291))
        self.pushButton_2start.setMaximumSize(QtCore.QSize(960, 720))
        self.pushButton_2start.setObjectName("pushButton_2")
        self.pushButton_3start = QtWidgets.QPushButton(Dialog)
        self.pushButton_3start.setGeometry(QtCore.QRect(280, 310, 401, 291))
        self.pushButton_3start.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2start.setText(_translate("Dialog", "Load project"))
        self.pushButton_3start.setText(_translate("Dialog", "New Project"))
        #self.pushButton_3start.clicked.connect(self.event_config) 
        self.pushButton_3start.clicked.connect(self.openWindow) 
        self.pushButton_2start.clicked.connect(self.openWindowload) 


class Ui_Dialog_event(object):
    def openWindowteam(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_team()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowstartscreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)

        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 330, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 330, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 180, 191, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 140, 181, 51))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 190, 771, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 240, 211, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(780, 240, 211, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 230, 181, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 270, 181, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(760, 280, 51, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(760, 240, 51, 41))
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(540, 280, 211, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(780, 280, 211, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(540, 40, 541, 51))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        
        ####
        self.pushButton_2.clicked.connect(self.openWindowteam) 
        self.pushButton.clicked.connect(self.openWindowstartscreen) 
        ####


        self.pushButton_2.setText(_translate("Dialog", "Save Event"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type your descripition here...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Description</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Dialog", "Name of project"))
        self.lineEdit_3.setText(_translate("Dialog", "Date- MM/DD/YYYY"))
        self.lineEdit_4.setText(_translate("Dialog", "Time- HH:MM"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event Start:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event end:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">-</span></p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">-</span></p><p><br/></p></body></html>"))
        self.lineEdit_7.setText(_translate("Dialog", "Date- MM/DD/YYYY"))
        self.lineEdit_6.setText(_translate("Dialog", "Time- HH:MM"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event Configuration</span></p></body></html>"))

class Ui_Dialog_team(object):
       
    def openWindowdirectory(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialogdirectory()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(540, 20, 541, 51))
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(70, 210, 131, 61))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 220, 771, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 260, 721, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(150, 310, 721, 51))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 370, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 370, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Team Configuration</span></p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Lead"))
        self.lineEdit_2.setText(_translate("Dialog", "Lead ip adress:"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><a name=\"docs-internal-guid-2f1a036e-7fff-714c-aa06-bad754901a57\"/><span style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; color:#000000; background-color:transparent;\">N</span><span style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; color:#000000; background-color:transparent;\">o. of established connections to the lead’s IP address: ##</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; color:#000000; background-color:transparent;\">No. of connections to the lead’s IP address: ##</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.setText(_translate("Dialog", "Connect"))
        self.pushButton_2.clicked.connect(self.openWindowdirectory) 

class Ui_Loadprject(object):
    
    def setupUi(self, Loadprject):
        Loadprject.setObjectName("Loadprject")
        Loadprject.resize(1280, 764)
        Loadprject.setMinimumSize(QtCore.QSize(1280, 720))
        self.textBrowser = QtWidgets.QTextBrowser(Loadprject)
        self.textBrowser.setGeometry(QtCore.QRect(240, 570, 851, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Loadprject)
        self.pushButton.setGeometry(QtCore.QRect(240, 620, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Loadprject)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 620, 211, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Loadprject)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 570, 93, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Loadprject)
        QtCore.QMetaObject.connectSlotsByName(Loadprject)

    def retranslateUi(self, Loadprject):
        _translate = QtCore.QCoreApplication.translate
        Loadprject.setWindowTitle(_translate("Loadprject", "Dialog"))
        self.textBrowser.setHtml(_translate("Loadprject", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Loadprject", "Cancel"))
        self.pushButton_3.setText(_translate("Loadprject", "Open"))
        self.pushButton_2.setText(_translate("Loadprject", "Browse"))


class Ui_Dialogdirectory(object):
    
    def openWindowvector001(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_vector001()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(510, 40, 541, 51))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 200, 771, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 240, 771, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 280, 771, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 320, 771, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 370, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 370, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 200, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 240, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 280, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 320, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Directory Configuration</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Dialog", "Root directory"))
        self.lineEdit_3.setText(_translate("Dialog", "Red Team Folder"))
        self.lineEdit_4.setText(_translate("Dialog", "Blue Team Folder"))
        self.lineEdit_5.setText(_translate("Dialog", "White Team Folder"))
        self.pushButton_2.setText(_translate("Dialog", "Start Data Ingestion"))
        
        self.pushButton_2.clicked.connect(self.openWindowvector001)


        self.pushButton_3.setText(_translate("Dialog", "Cancel "))
        self.pushButton_4.setText(_translate("Dialog", "Broswe"))
        self.pushButton_5.setText(_translate("Dialog", "Broswe"))
        self.pushButton_6.setText(_translate("Dialog", "Broswe"))
        self.pushButton_7.setText(_translate("Dialog", "Broswe"))


class Ui_Dialog_vector001(object):
    def openWindowexport(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_export()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowfilter(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_filter()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowgraphbuilder(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_uiGraphBuilder()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindownodeconfig(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_uiNodeConfigurationGraphical()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def openWindowchangeconfig(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_uiChangeConfiguration()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowtabular(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_uiNodeConfigurationTabularFormat()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowrelationship(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_relationship()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowicon(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_iconconfig()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowlogentry(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_logentry()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def openWindowvectorDB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_vectorDB()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 30, 541, 51))
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(90, 140, 391, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(8, 0, item)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 520, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 520, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 520, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(220, 160, 21, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(220, 180, 21, 21))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(350, 180, 21, 21))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(350, 160, 21, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.filter_config_button = QtWidgets.QPushButton(Dialog)
        self.filter_config_button.setGeometry(QtCore.QRect(670, 210, 281, 32))
        self.filter_config_button.setObjectName("filter_config_button")
        self.export_config_button = QtWidgets.QPushButton(Dialog)
        self.export_config_button.setGeometry(QtCore.QRect(670, 230, 281, 32))
        self.export_config_button.setObjectName("export_config_button")
        self.graph_builder_config_button = QtWidgets.QPushButton(Dialog)
        self.graph_builder_config_button.setGeometry(QtCore.QRect(670, 250, 281, 32))
        self.graph_builder_config_button.setObjectName("graph_builder_config_button")
        self.relationship_config_button = QtWidgets.QPushButton(Dialog)
        self.relationship_config_button.setGeometry(QtCore.QRect(670, 370, 281, 32))
        self.relationship_config_button.setObjectName("relationship_config_button")
        self.node_config_graph_button = QtWidgets.QPushButton(Dialog)
        self.node_config_graph_button.setGeometry(QtCore.QRect(670, 290, 281, 32))
        self.node_config_graph_button.setObjectName("node_config_graph_button")
        self.change_config_button = QtWidgets.QPushButton(Dialog)
        self.change_config_button.setGeometry(QtCore.QRect(670, 330, 281, 32))
        self.change_config_button.setObjectName("change_config_button")
        self.node_config_table_button = QtWidgets.QPushButton(Dialog)
        self.node_config_table_button.setGeometry(QtCore.QRect(670, 310, 281, 32))
        self.node_config_table_button.setObjectName("node_config_table_button")
        self.icon_config_button = QtWidgets.QPushButton(Dialog)
        self.icon_config_button.setGeometry(QtCore.QRect(670, 390, 281, 32))
        self.icon_config_button.setObjectName("icon_config_button")
        self.log_entry_config_button = QtWidgets.QPushButton(Dialog)
        self.log_entry_config_button.setGeometry(QtCore.QRect(980, 210, 221, 32))
        self.log_entry_config_button.setObjectName("log_entry_config_button")
        self.vector_db_config = QtWidgets.QPushButton(Dialog)
        self.vector_db_config.setGeometry(QtCore.QRect(980, 230, 221, 32))
        self.vector_db_config.setObjectName("vector_db_config")
        self.vector_db_lead_button = QtWidgets.QPushButton(Dialog)
        self.vector_db_lead_button.setGeometry(QtCore.QRect(980, 250, 221, 32))
        self.vector_db_lead_button.setObjectName("vector_db_lead_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Vector Configuration</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Vector Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Description"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("Dialog", "Delete Vector"))
        self.pushButton_4.setText(_translate("Dialog", "Edit Vector"))
        self.pushButton_5.setText(_translate("Dialog", "Add Vector"))
        self.toolButton.setText(_translate("Dialog", "↑    "))
        self.toolButton_3.setText(_translate("Dialog", "↓"))
        self.toolButton_4.setText(_translate("Dialog", "↓"))
        self.toolButton_2.setText(_translate("Dialog", "↑    "))

        self.filter_config_button.clicked.connect(self.openWindowfilter)
        self.filter_config_button.setText(_translate("Dialog", "filter configuration"))
        
        self.export_config_button.setText(_translate("Dialog", "export configuration"))
        self.export_config_button.clicked.connect(self.openWindowexport)



        self.graph_builder_config_button.setText(_translate("Dialog", "graph builder configuration"))
        self.graph_builder_config_button.clicked.connect(self.openWindowgraphbuilder)

        self.relationship_config_button.setText(_translate("Dialog", "relationship configuration"))
        self.relationship_config_button.clicked.connect(self.openWindowrelationship)

        self.node_config_graph_button.setText(_translate("Dialog", "node configuration in graph"))
        self.node_config_graph_button.clicked.connect(self.openWindownodeconfig)

        self.change_config_button.setText(_translate("Dialog", "change configuration"))
        self.change_config_button.clicked.connect(self.openWindowchangeconfig)

        self.node_config_table_button.setText(_translate("Dialog", "node configuration in tabular"))
        self.node_config_table_button.clicked.connect(self.openWindowtabular)

        self.icon_config_button.setText(_translate("Dialog", "icon configuration"))
        self.icon_config_button.clicked.connect(self.openWindowicon)

        self.log_entry_config_button.setText(_translate("Dialog", "log entry configuration"))
        self.log_entry_config_button.clicked.connect(self.openWindowlogentry)

        self.vector_db_config.setText(_translate("Dialog", "vector DB configuration"))
        self.vector_db_config.clicked.connect(self.openWindowvectorDB)

        self.vector_db_lead_button.setText(_translate("Dialog", "vector DB lead"))


class Ui_Dialog_export(object):
    
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 50, 541, 51))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(620, 210, 131, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480, 210, 131, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Export Configuration</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Export Format"))
        self.pushButton.setText(_translate("Dialog", "Export"))
        self.pushButton.clicked.connect(self.openWindowhelper)


class Ui_Dialog_helper(object):

    def openWindowvector001(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_vector001()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(510, 360, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.okay_button = QtWidgets.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(650, 360, 113, 32))
        self.okay_button.setObjectName("okay_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 110, 641, 221))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel_button.setText(_translate("Dialog", "cancel"))
        self.okay_button.setText(_translate("Dialog", "okay"))
        self.label.setText(_translate("Dialog", "Are you sure?"))
        self.okay_button.clicked.connect(self.openWindowvector001)
        self.cancel_button.clicked.connect(self.openWindowvector001)


class Ui_Dialog_filter(object):

    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(500, 40, 541, 51))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 520, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 520, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 250, 771, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(190, 270, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 270, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 270, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 220, 121, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(140, 330, 181, 31))
        self.label_8.setObjectName("label_8")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(70, 380, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(290, 380, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(180, 380, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 410, 181, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 420, 211, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 420, 211, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(460, 420, 51, 41))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 450, 181, 51))
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 460, 211, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(460, 460, 51, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 460, 211, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Filter Configuration</span></p></body></html>"))
        
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.setText(_translate("Dialog", "Apply Filter"))

        self.pushButton.clicked.connect(self.openWindowhelper)
        self.pushButton_2.clicked.connect(self.openWindowhelper)

        self.lineEdit_2.setText(_translate("Dialog", "Keyword Search"))
        self.radioButton.setText(_translate("Dialog", "Blue Team"))
        self.radioButton_2.setText(_translate("Dialog", "White Team"))
        self.radioButton_3.setText(_translate("Dialog", "Red Team"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Creator</span></p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event Type</span></p><p><br/></p><p><br/></p></body></html>"))
        self.radioButton_4.setText(_translate("Dialog", "Red Team"))
        self.radioButton_5.setText(_translate("Dialog", "White Team"))
        self.radioButton_6.setText(_translate("Dialog", "Blue Team"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event Start:</span></p></body></html>"))
        self.lineEdit_3.setText(_translate("Dialog", "Date- MM/DD/YYYY"))
        self.lineEdit_4.setText(_translate("Dialog", "Time- HH:MM"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">-</span></p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Event end:</span></p></body></html>"))
        self.lineEdit_7.setText(_translate("Dialog", "Date- MM/DD/YYYY"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">-</span></p><p><br/></p></body></html>"))
        self.lineEdit_6.setText(_translate("Dialog", "Time- HH:MM"))


class Ui_uiGraphBuilder(object):

    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(980, 720)
        Dialog.setMinimumSize(QtCore.QSize(980, 720))
        Dialog.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 190, 81, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(310, 190, 361, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 240, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 240, 411, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 500, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 540, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 500, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 540, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 500, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 540, 111, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Graph Builder Configuration"))
        self.label_2.setText(_translate("Dialog", "Vector:"))
        self.label_3.setText(_translate("Dialog", "Description:"))
        self.label_4.setText(_translate("Dialog", "This is a vector description"))
        
        
        self.pushButton.setText(_translate("Dialog", "Add Node"))
        self.pushButton.clicked.connect(self.openWindowhelper)

        self.pushButton_2.setText(_translate("Dialog", "Add Relationship"))
        self.pushButton_2.clicked.connect(self.openWindowhelper)

        self.pushButton_3.setText(_translate("Dialog", "Delete Node"))
        self.pushButton_3.clicked.connect(self.openWindowhelper)

        self.pushButton_4.setText(_translate("Dialog", "Delete Relationship"))
        self.pushButton_4.clicked.connect(self.openWindowhelper)

        self.pushButton_5.setText(_translate("Dialog", "Edit Node"))
        self.pushButton_6.setText(_translate("Dialog", "Edit Relationship"))


class Ui_uiNodeConfigurationGraphical(object):

    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()

    def setupUi(self, uiNodeConfigurationGraphical):
        uiNodeConfigurationGraphical.setObjectName("uiNodeConfigurationGraphical")
        uiNodeConfigurationGraphical.resize(980, 720)
        uiNodeConfigurationGraphical.setMinimumSize(QtCore.QSize(980, 720))
        uiNodeConfigurationGraphical.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label.setGeometry(QtCore.QRect(40, 30, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox.setGeometry(QtCore.QRect(162, 658, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_2.setGeometry(QtCore.QRect(50, 660, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox_2.setGeometry(QtCore.QRect(162, 98, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 101, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton.setGeometry(QtCore.QRect(500, 660, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 660, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(uiNodeConfigurationGraphical)
        self.graphicsView.setGeometry(QtCore.QRect(160, 140, 681, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(uiNodeConfigurationGraphical)
        self.line.setGeometry(QtCore.QRect(160, 630, 681, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(uiNodeConfigurationGraphical)
        self.lineEdit.setGeometry(QtCore.QRect(350, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_4.setGeometry(QtCore.QRect(290, 100, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(uiNodeConfigurationGraphical)
        QtCore.QMetaObject.connectSlotsByName(uiNodeConfigurationGraphical)

    def retranslateUi(self, uiNodeConfigurationGraphical):
        _translate = QtCore.QCoreApplication.translate
        uiNodeConfigurationGraphical.setWindowTitle(_translate("uiNodeConfigurationGraphical", "Dialog"))
        self.label.setText(_translate("uiNodeConfigurationGraphical", "Nodes configuration in graphical format"))
        self.comboBox.setItemText(0, _translate("uiNodeConfigurationGraphical", "Horizontal"))
        self.comboBox.setItemText(1, _translate("uiNodeConfigurationGraphical", "Vertical"))
        self.label_2.setText(_translate("uiNodeConfigurationGraphical", "Timeline orientation:"))
        self.comboBox_2.setItemText(0, _translate("uiNodeConfigurationGraphical", "Hours"))
        self.comboBox_2.setItemText(1, _translate("uiNodeConfigurationGraphical", "Minutes"))
        self.comboBox_2.setItemText(2, _translate("uiNodeConfigurationGraphical", "Seconds"))
        self.label_3.setText(_translate("uiNodeConfigurationGraphical", "Interval units:"))
        self.pushButton.setText(_translate("uiNodeConfigurationGraphical", "Zoom in"))
        self.pushButton_2.setText(_translate("uiNodeConfigurationGraphical", "Zoom out"))
        self.label_4.setText(_translate("uiNodeConfigurationGraphical", "Interval:"))


class Ui_uiChangeConfiguration(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, uiChangeConfiguration):
        uiChangeConfiguration.setObjectName("uiChangeConfiguration")
        uiChangeConfiguration.resize(980, 720)
        uiChangeConfiguration.setMinimumSize(QtCore.QSize(980, 720))
        uiChangeConfiguration.setMaximumSize(QtCore.QSize(980, 720))
        self.pushButton = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton.setGeometry(QtCore.QRect(420, 660, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 660, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(uiChangeConfiguration)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(uiChangeConfiguration)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 90, 761, 541))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 71, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(uiChangeConfiguration)
        QtCore.QMetaObject.connectSlotsByName(uiChangeConfiguration)

    def retranslateUi(self, uiChangeConfiguration):
        _translate = QtCore.QCoreApplication.translate
        uiChangeConfiguration.setWindowTitle(_translate("uiChangeConfiguration", "Dialog"))
        self.pushButton.setText(_translate("uiChangeConfiguration", "Undo"))

        self.pushButton_2.setText(_translate("uiChangeConfiguration", "Commit"))
        self.pushButton_2.clicked.connect(self.openWindowhelper)

        self.label.setText(_translate("uiChangeConfiguration", "Change Configuration"))
        self.label_2.setText(_translate("uiChangeConfiguration", "Change List:"))


class Ui_uiNodeConfigurationTabularFormat(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, uiNodeConfigurationTabularFormat):
        uiNodeConfigurationTabularFormat.setObjectName("uiNodeConfigurationTabularFormat")
        uiNodeConfigurationTabularFormat.resize(980, 720)
        uiNodeConfigurationTabularFormat.setMinimumSize(QtCore.QSize(980, 720))
        uiNodeConfigurationTabularFormat.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(uiNodeConfigurationTabularFormat)
        self.label.setGeometry(QtCore.QRect(40, 30, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(uiNodeConfigurationTabularFormat)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 921, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)

        self.retranslateUi(uiNodeConfigurationTabularFormat)
        QtCore.QMetaObject.connectSlotsByName(uiNodeConfigurationTabularFormat)

    def retranslateUi(self, uiNodeConfigurationTabularFormat):
        _translate = QtCore.QCoreApplication.translate
        uiNodeConfigurationTabularFormat.setWindowTitle(_translate("uiNodeConfigurationTabularFormat", "Dialog"))
        self.label.setText(_translate("uiNodeConfigurationTabularFormat", "Nodes configuration in tabular format"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "+"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Node property visibility"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Node name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Node timestamp"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Node description"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Log entry reference"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Log creator"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Event type"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Icon type"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Source"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("uiNodeConfigurationTabularFormat", "Node visibility"))


class Ui_relationship(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, uiNodeConfigurationGraphical):
        uiNodeConfigurationGraphical.setObjectName("uiNodeConfigurationGraphical")
        uiNodeConfigurationGraphical.resize(980, 720)
        uiNodeConfigurationGraphical.setMinimumSize(QtCore.QSize(980, 720))
        uiNodeConfigurationGraphical.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label.setGeometry(QtCore.QRect(40, 30, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox.setGeometry(QtCore.QRect(162, 658, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_2.setGeometry(QtCore.QRect(50, 660, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox_2.setGeometry(QtCore.QRect(162, 98, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 101, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton.setGeometry(QtCore.QRect(500, 660, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 660, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(uiNodeConfigurationGraphical)
        self.graphicsView.setGeometry(QtCore.QRect(160, 140, 681, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(uiNodeConfigurationGraphical)
        self.line.setGeometry(QtCore.QRect(160, 630, 681, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(uiNodeConfigurationGraphical)
        self.lineEdit.setGeometry(QtCore.QRect(350, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_4.setGeometry(QtCore.QRect(290, 100, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(uiNodeConfigurationGraphical)
        QtCore.QMetaObject.connectSlotsByName(uiNodeConfigurationGraphical)

    def retranslateUi(self, uiNodeConfigurationGraphical):
        _translate = QtCore.QCoreApplication.translate
        uiNodeConfigurationGraphical.setWindowTitle(_translate("uiNodeConfigurationGraphical", "Dialog"))
        self.label.setText(_translate("uiNodeConfigurationGraphical", "Relationship Configuration"))
        self.comboBox.setItemText(0, _translate("uiNodeConfigurationGraphical", "Horizontal"))
        self.comboBox.setItemText(1, _translate("uiNodeConfigurationGraphical", "Vertical"))
        self.label_2.setText(_translate("uiNodeConfigurationGraphical", "Timeline orientation:"))
        self.comboBox_2.setItemText(0, _translate("uiNodeConfigurationGraphical", "Hours"))
        self.comboBox_2.setItemText(1, _translate("uiNodeConfigurationGraphical", "Minutes"))
        self.comboBox_2.setItemText(2, _translate("uiNodeConfigurationGraphical", "Seconds"))
        self.label_3.setText(_translate("uiNodeConfigurationGraphical", "Interval units:"))
        self.pushButton.setText(_translate("uiNodeConfigurationGraphical", "Zoom in"))
        self.pushButton_2.setText(_translate("uiNodeConfigurationGraphical", "Zoom out"))
        self.label_4.setText(_translate("uiNodeConfigurationGraphical", "Interval:"))


class Ui_iconconfig(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, uiChangeConfiguration):
        uiChangeConfiguration.setObjectName("uiChangeConfiguration")
        uiChangeConfiguration.resize(980, 720)
        uiChangeConfiguration.setMinimumSize(QtCore.QSize(980, 720))
        uiChangeConfiguration.setMaximumSize(QtCore.QSize(980, 720))
        self.pushButton = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton.setGeometry(QtCore.QRect(370, 640, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(uiChangeConfiguration)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 640, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 640, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(uiChangeConfiguration)
        self.tableWidget.setGeometry(QtCore.QRect(110, 90, 761, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(uiChangeConfiguration)
        QtCore.QMetaObject.connectSlotsByName(uiChangeConfiguration)

    def retranslateUi(self, uiChangeConfiguration):
        _translate = QtCore.QCoreApplication.translate
        uiChangeConfiguration.setWindowTitle(_translate("uiChangeConfiguration", "Dialog"))
        
        self.pushButton.setText(_translate("uiChangeConfiguration", "Delete Icon"))
        self.pushButton.clicked.connect(self.openWindowhelper)

        self.label.setText(_translate("uiChangeConfiguration", "Icon Configuration"))
        
        self.pushButton_4.setText(_translate("uiChangeConfiguration", "Add Icon"))
        self.pushButton_4.clicked.connect(self.openWindowhelper)

        self.pushButton_6.setText(_translate("uiChangeConfiguration", "Edit Icon"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "+"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Icon name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("uiChangeConfiguration", "Icon source"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("uiChangeConfiguration", "Image preview"))


class Ui_logentry(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 787)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(90, 180, 1011, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(8, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(460, 40, 541, 51))
        self.label_6.setObjectName("label_6")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(310, 220, 20, 21))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(310, 200, 21, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_5 = QtWidgets.QToolButton(Dialog)
        self.toolButton_5.setGeometry(QtCore.QRect(510, 220, 20, 21))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(510, 200, 21, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(710, 190, 21, 21))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_6 = QtWidgets.QToolButton(Dialog)
        self.toolButton_6.setGeometry(QtCore.QRect(710, 210, 20, 21))
        self.toolButton_6.setObjectName("toolButton_6")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(960, 250, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(960, 440, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(960, 400, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(960, 370, 73, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(960, 330, 73, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(960, 290, 73, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(960, 510, 73, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(Dialog)
        self.comboBox_8.setGeometry(QtCore.QRect(960, 480, 73, 22))
        self.comboBox_8.setObjectName("comboBox_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "List Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Log Entry Timestamp"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Log Entry Event"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Vector"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Log Entry Configuration</span></p></body></html>"))
        self.toolButton_4.setText(_translate("Dialog", "↓"))
        self.toolButton.setText(_translate("Dialog", "↑    "))
        self.toolButton_5.setText(_translate("Dialog", "↓"))
        self.toolButton_2.setText(_translate("Dialog", "↑    "))
        self.toolButton_3.setText(_translate("Dialog", "↑    "))
        self.toolButton_6.setText(_translate("Dialog", "↓"))


class Ui_vectorDB(object):
    def openWindowhelper(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_helper()
        self.ui.setupUi(self.window)
        Dialog.hide() # ISSUE: Dialog.hide() not recognized within the program; Python recognizes it separately
        self.window.show()
    def setupUi(self, uiChangeConfiguration):
        uiChangeConfiguration.setObjectName("uiChangeConfiguration")
        uiChangeConfiguration.resize(980, 720)
        uiChangeConfiguration.setMinimumSize(QtCore.QSize(980, 720))
        uiChangeConfiguration.setMaximumSize(QtCore.QSize(980, 720))
        self.pushButton = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton.setGeometry(QtCore.QRect(220, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 650, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(uiChangeConfiguration)
        self.label.setGeometry(QtCore.QRect(40, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 141, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 161, 20))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(uiChangeConfiguration)
        self.tableWidget.setGeometry(QtCore.QRect(50, 160, 411, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_5 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_5.setGeometry(QtCore.QRect(490, 130, 161, 20))
        self.label_5.setObjectName("label_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(uiChangeConfiguration)
        self.tableWidget_2.setGeometry(QtCore.QRect(490, 160, 431, 481))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        self.retranslateUi(uiChangeConfiguration)
        QtCore.QMetaObject.connectSlotsByName(uiChangeConfiguration)

    def retranslateUi(self, uiChangeConfiguration):
        _translate = QtCore.QCoreApplication.translate
        uiChangeConfiguration.setWindowTitle(_translate("uiChangeConfiguration", "Dialog"))
        
        self.pushButton.setText(_translate("uiChangeConfiguration", "Pull"))
        self.pushButton.clicked.connect(self.openWindowhelper)

        self.pushButton_2.setText(_translate("uiChangeConfiguration", "Push"))
        self.pushButton_2.clicked.connect(self.openWindowhelper)
        
        self.label.setText(_translate("uiChangeConfiguration", "Vector Database Configuration"))
        self.label_2.setText(_translate("uiChangeConfiguration", "Connection Status to lead:"))
        self.label_3.setText(_translate("uiChangeConfiguration", "Connected"))
        self.label_4.setText(_translate("uiChangeConfiguration", "Pulled vector DB table (Analyst)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "+"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Vector"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("uiChangeConfiguration", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("uiChangeConfiguration", "Graph"))
        self.label_5.setText(_translate("uiChangeConfiguration", "Pushed vector DB table (Analyst)"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "+"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Vector"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("uiChangeConfiguration", "Description"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("uiChangeConfiguration", "Graph"))



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
