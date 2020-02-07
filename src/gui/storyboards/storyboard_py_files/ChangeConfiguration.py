# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/ChangeConfiguration.ui'
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
        self.label.setText(_translate("uiChangeConfiguration", "Change Configuration"))
        self.label_2.setText(_translate("uiChangeConfiguration", "Change List:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiChangeConfiguration = QtWidgets.QDialog()
    ui = Ui_uiChangeConfiguration()
    ui.setupUi(uiChangeConfiguration)
    uiChangeConfiguration.show()
    sys.exit(app.exec_())
