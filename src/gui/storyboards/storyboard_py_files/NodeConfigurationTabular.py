# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/NodeConfigurationTabular.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uiNodeConfigurationTabularFormat(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiNodeConfigurationTabularFormat = QtWidgets.QDialog()
    ui = Ui_uiNodeConfigurationTabularFormat()
    ui.setupUi(uiNodeConfigurationTabularFormat)
    uiNodeConfigurationTabularFormat.show()
    sys.exit(app.exec_())
