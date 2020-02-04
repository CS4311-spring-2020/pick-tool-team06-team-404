# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/helper_page.ui'
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
