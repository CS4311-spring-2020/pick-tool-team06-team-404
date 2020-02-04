# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/TeamConfig.ui'
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
