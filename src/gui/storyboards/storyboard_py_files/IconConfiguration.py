# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/IconConfiguration.ui'
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
        self.label.setText(_translate("uiChangeConfiguration", "Icon Configuration"))
        self.pushButton_4.setText(_translate("uiChangeConfiguration", "Add Icon"))
        self.pushButton_6.setText(_translate("uiChangeConfiguration", "Edit Icon"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("uiChangeConfiguration", "+"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("uiChangeConfiguration", "Icon name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("uiChangeConfiguration", "Icon source"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("uiChangeConfiguration", "Image preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiChangeConfiguration = QtWidgets.QDialog()
    ui = Ui_uiChangeConfiguration()
    ui.setupUi(uiChangeConfiguration)
    uiChangeConfiguration.show()
    sys.exit(app.exec_())
