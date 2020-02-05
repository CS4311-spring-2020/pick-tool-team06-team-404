# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/VectorDBConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uiChangeConfiguration(object):
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
        self.pushButton_2.setText(_translate("uiChangeConfiguration", "Push"))
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiChangeConfiguration = QtWidgets.QDialog()
    ui = Ui_uiChangeConfiguration()
    ui.setupUi(uiChangeConfiguration)
    uiChangeConfiguration.show()
    sys.exit(app.exec_())
