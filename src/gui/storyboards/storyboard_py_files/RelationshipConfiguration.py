# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mmedina-a/Desktop/ui/RelationshipConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uiNodeConfigurationGraphical(object):
    def setupUi(self, uiNodeConfigurationGraphical):
        uiNodeConfigurationGraphical.setObjectName("uiNodeConfigurationGraphical")
        uiNodeConfigurationGraphical.resize(980, 720)
        uiNodeConfigurationGraphical.setMinimumSize(QtCore.QSize(980, 720))
        uiNodeConfigurationGraphical.setMaximumSize(QtCore.QSize(980, 720))
        self.label = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label.setGeometry(QtCore.QRect(40, 30, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox.setGeometry(QtCore.QRect(162, 658, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_2.setGeometry(QtCore.QRect(50, 660, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(uiNodeConfigurationGraphical)
        self.comboBox_2.setGeometry(QtCore.QRect(162, 98, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 101, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton.setGeometry(QtCore.QRect(500, 660, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(uiNodeConfigurationGraphical)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 660, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(uiNodeConfigurationGraphical)
        self.graphicsView.setGeometry(QtCore.QRect(160, 140, 681, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(uiNodeConfigurationGraphical)
        self.line.setGeometry(QtCore.QRect(160, 630, 681, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(uiNodeConfigurationGraphical)
        self.lineEdit.setGeometry(QtCore.QRect(350, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(uiNodeConfigurationGraphical)
        self.label_4.setGeometry(QtCore.QRect(290, 100, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(uiNodeConfigurationGraphical)
        QtCore.QMetaObject.connectSlotsByName(uiNodeConfigurationGraphical)

    def retranslateUi(self, uiNodeConfigurationGraphical):
        _translate = QtCore.QCoreApplication.translate
        uiNodeConfigurationGraphical.setWindowTitle(_translate("uiNodeConfigurationGraphical", "Dialog"))
        self.label.setText(_translate("uiNodeConfigurationGraphical", "Nodes configuration in graphical format"))
        self.comboBox.setItemText(0, _translate("uiNodeConfigurationGraphical", "Horizontal"))
        self.comboBox.setItemText(1, _translate("uiNodeConfigurationGraphical", "Vertical"))
        self.label_2.setText(_translate("uiNodeConfigurationGraphical", "Timeline orientation:"))
        self.comboBox_2.setItemText(0, _translate("uiNodeConfigurationGraphical", "Hours"))
        self.comboBox_2.setItemText(1, _translate("uiNodeConfigurationGraphical", "Minutes"))
        self.comboBox_2.setItemText(2, _translate("uiNodeConfigurationGraphical", "Seconds"))
        self.label_3.setText(_translate("uiNodeConfigurationGraphical", "Interval units:"))
        self.pushButton.setText(_translate("uiNodeConfigurationGraphical", "Zoom in"))
        self.pushButton_2.setText(_translate("uiNodeConfigurationGraphical", "Zoom out"))
        self.label_4.setText(_translate("uiNodeConfigurationGraphical", "Interval:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiNodeConfigurationGraphical = QtWidgets.QDialog()
    ui = Ui_uiNodeConfigurationGraphical()
    ui.setupUi(uiNodeConfigurationGraphical)
    uiNodeConfigurationGraphical.show()
    sys.exit(app.exec_())
