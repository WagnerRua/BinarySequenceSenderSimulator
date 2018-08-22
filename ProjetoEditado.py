# -*- coding: utf-8 -*-
#Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

# Form implementation generated from reading ui file 'ModeloQTDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#Funcao que converte strings para uma string de numeros binarios.
def toBin(st):
    string = ''
    for x in st:
        string +=  format(ord(x), 'b') + " "
    
    return string

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
	#Configuracoes do campo para digitar a mensagem.
        self.messageEditor = QtWidgets.QLineEdit(self.centralwidget)
        self.messageEditor.setObjectName("messageEditor")
        self.horizontalLayout.addWidget(self.messageEditor)
	#Configuracoes do botao.
        self.sendMessageButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.horizontalLayout.addWidget(self.sendMessageButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
	
	#Configuracoes da primeira linha de separacao.
	self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
	
	#Configuracoes do label da mensagem.
	self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
	self.messageLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.messageLabel)

	#Configuracoes da segunda linha de separacao.
	self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

	#Configuracoes do label da mensagem em binario.
	self.binaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.binaryLabel.setText("")
        self.binaryLabel.setObjectName("binaryLabel")
        self.binaryLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.binaryLabel)

	#Configuracoes da terceira linha de separacao.
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
  
        #Configuracoes do label da mensagem codificada.
        self.encodedLabel = QtWidgets.QLabel(self.centralwidget)
        self.encodedLabel.setText("")
        self.encodedLabel.setObjectName("encodedLabel")
	self.encodedLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.encodedLabel)

	#Configuracoes da quarta linha de separacao.
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
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
        self.sendMessageButton.setText(_translate("MainWindow", "Send Message"))

    def refresh_Labels(self, MainWindow):
	_translate = QtCore.QCoreApplication.translate        
        string = self.messageEditor.text()
        binary_string = toBin(string) #Covertemos a string que esta na caixa de mensagens para binario.
        self.messageLabel.setText(_translate("MainWindow", string)) #Repetimos a mensagem no label coreto.                                                                         
        self.binaryLabel.setText(_translate("MainWindow", binary_string)) #Colocamos o codigo binario no label correto.

    #Quando o botão for pressionado chamamos a função para atualizar os labels.
    def button_Clicked(self, MainWindow):
        self.sendMessageButton.clicked.connect(self.refresh_Labels)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_Clicked(MainWindow) #Se o botao for pressionado.
    MainWindow.show()
    sys.exit(app.exec_())

