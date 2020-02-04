# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/LogFileConfiguration.ui'
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
        self.label = QtWidgets.QLabel(uiChangeConfiguration)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(uiChangeConfiguration)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 421, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.label_2 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 47, 21))
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(uiChangeConfiguration)
        self.tableWidget_2.setGeometry(QtCore.QRect(510, 120, 421, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 231, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(uiChangeConfiguration)
        self.label_4.setGeometry(QtCore.QRect(570, 90, 231, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton.setGeometry(QtCore.QRect(720, 640, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiChangeConfiguration)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 640, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(uiChangeConfiguration)
        QtCore.QMetaObject.connectSlotsByName(uiChangeConfiguration)

    def retranslateUi(self, uiChangeConfiguration):
        _translate = QtCore.QCoreApplication.translate
        uiChangeConfiguration.setWindowTitle(_translate("uiChangeConfiguration", "Dialog"))
        self.label.setText(_translate("uiChangeConfiguration", "Log file configuration"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "File name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("uiChangeConfiguration", "Cleansing status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("uiChangeConfiguration", "Validation status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("uiChangeConfiguration", "Ingestion status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("uiChangeConfiguration", "View enforcement action report"))
        self.label_2.setText(_translate("uiChangeConfiguration", "Log files:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "Line number"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Error message"))
        self.label_3.setText(_translate("uiChangeConfiguration", "File name:"))
        self.label_4.setText(_translate("uiChangeConfiguration", "file.txt"))
        self.pushButton.setText(_translate("uiChangeConfiguration", "Validate"))
        self.pushButton_2.setText(_translate("uiChangeConfiguration", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiChangeConfiguration = QtWidgets.QDialog()
    ui = Ui_uiChangeConfiguration()
    ui.setupUi(uiChangeConfiguration)
    uiChangeConfiguration.show()
    sys.exit(app.exec_())
