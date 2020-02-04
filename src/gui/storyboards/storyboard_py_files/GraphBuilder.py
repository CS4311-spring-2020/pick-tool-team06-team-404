# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/GraphBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uiGraphBuilder(object):
    def setupUi(self, uiGraphBuilder):
        uiGraphBuilder.setObjectName("uiGraphBuilder")
        uiGraphBuilder.resize(980, 720)
        uiGraphBuilder.setMinimumSize(QtCore.QSize(980, 720))
        uiGraphBuilder.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(uiGraphBuilder)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(uiGraphBuilder)
        self.label_2.setGeometry(QtCore.QRect(270, 190, 81, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(uiGraphBuilder)
        self.comboBox.setGeometry(QtCore.QRect(310, 190, 361, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(uiGraphBuilder)
        self.label_3.setGeometry(QtCore.QRect(250, 240, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(uiGraphBuilder)
        self.label_4.setGeometry(QtCore.QRect(320, 240, 411, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton.setGeometry(QtCore.QRect(300, 500, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 540, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 500, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 540, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 500, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(uiGraphBuilder)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 540, 111, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(uiGraphBuilder)
        QtCore.QMetaObject.connectSlotsByName(uiGraphBuilder)

    def retranslateUi(self, uiGraphBuilder):
        _translate = QtCore.QCoreApplication.translate
        uiGraphBuilder.setWindowTitle(_translate("uiGraphBuilder", "Dialog"))
        self.label.setText(_translate("uiGraphBuilder", "Graph Builder Configuration"))
        self.label_2.setText(_translate("uiGraphBuilder", "Vector:"))
        self.label_3.setText(_translate("uiGraphBuilder", "Description:"))
        self.label_4.setText(_translate("uiGraphBuilder", "This is a vector description"))
        self.pushButton.setText(_translate("uiGraphBuilder", "Add Node"))
        self.pushButton_2.setText(_translate("uiGraphBuilder", "Add Relationship"))
        self.pushButton_3.setText(_translate("uiGraphBuilder", "Delete Node"))
        self.pushButton_4.setText(_translate("uiGraphBuilder", "Delete Relationship"))
        self.pushButton_5.setText(_translate("uiGraphBuilder", "Edit Node"))
        self.pushButton_6.setText(_translate("uiGraphBuilder", "Edit Relationship"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiGraphBuilder = QtWidgets.QDialog()
    ui = Ui_uiGraphBuilder()
    ui.setupUi(uiGraphBuilder)
    uiGraphBuilder.show()
    sys.exit(app.exec_())
