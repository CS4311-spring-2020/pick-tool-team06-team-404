# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Load project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loadprject = QtWidgets.QDialog()
    ui = Ui_Loadprject()
    ui.setupUi(Loadprject)
    Loadprject.show()
    sys.exit(app.exec_())
