# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/ExportConfog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
