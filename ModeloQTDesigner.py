# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModeloQTDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageEditor = QtWidgets.QLineEdit(self.centralwidget)
        self.messageEditor.setObjectName("messageEditor")
        self.horizontalLayout.addWidget(self.messageEditor)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBoxNRZ = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxNRZ.setObjectName("checkBoxNRZ")
        self.horizontalLayout_5.addWidget(self.checkBoxNRZ)
        self.checkBoxNRZ_L = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxNRZ_L.setObjectName("checkBoxNRZ_L")
        self.horizontalLayout_5.addWidget(self.checkBoxNRZ_L)
        self.checkBoxNRZ_I = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxNRZ_I.setObjectName("checkBoxNRZ_I")
        self.horizontalLayout_5.addWidget(self.checkBoxNRZ_I)
        self.checkBoxZR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxZR.setObjectName("checkBoxZR")
        self.horizontalLayout_5.addWidget(self.checkBoxZR)
        self.pushButtonMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMessage.setObjectName("pushButtonMessage")
        self.horizontalLayout_5.addWidget(self.pushButtonMessage)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout.addWidget(self.line_1)
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout.addWidget(self.messageLabel)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.binaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.binaryLabel.setText("")
        self.binaryLabel.setObjectName("binaryLabel")
        self.verticalLayout.addWidget(self.binaryLabel)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.encodedLabel = QtWidgets.QLabel(self.centralwidget)
        self.encodedLabel.setText("")
        self.encodedLabel.setObjectName("encodedLabel")
        self.verticalLayout.addWidget(self.encodedLabel)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comunicação De Dados"))
        self.checkBoxNRZ.setText(_translate("MainWindow", "NRZ"))
        self.checkBoxNRZ_L.setText(_translate("MainWindow", "NRZ-L"))
        self.checkBoxNRZ_I.setText(_translate("MainWindow", "NRZ-I"))
        self.checkBoxZR.setText(_translate("MainWindow", "ZR"))
        self.pushButtonMessage.setText(_translate("MainWindow", "Send Message"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

