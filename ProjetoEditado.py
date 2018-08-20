#Alunos: Lucas da Silva Nolasco e Wagner Rodrigues Ulian Agostinho

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModeloAPS.ui'
#
# Created by: PyQt4 UI code generator 4.11.4

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Funcao que converte strings para uma string de numeros binarios.
def toBin(st):
    return (' '.join(format(ord(x), 'b') for x in str(st)))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        #Configuracoes do campo para digitar a mensagem.
        self.messageEditor = QtGui.QLineEdit(self.centralwidget)
        self.messageEditor.setObjectName(_fromUtf8("messageEditor"))
        self.horizontalLayout.addWidget(self.messageEditor)
        
        #Configuracoes do botao.
        self.sendMessageButton = QtGui.QPushButton(self.centralwidget)
        self.sendMessageButton.setObjectName(_fromUtf8("sendMessageButton"))
        self.horizontalLayout.addWidget(self.sendMessageButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        
        #Configuracoes da primeira linha de separacao.
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)

        #Configuracoes do label da mensagem.
        self.messageLabel = QtGui.QLabel(self.centralwidget)
        self.messageLabel.setText(_fromUtf8(""))
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.messageLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.messageLabel)
        

        #Configuracoes da segunda linha de separacao.
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)

        #Configuracoes do label da mensagem em binario.
        self.binaryLabel = QtGui.QLabel(self.centralwidget)
        self.binaryLabel.setText(_fromUtf8(""))
        self.binaryLabel.setObjectName(_fromUtf8("binaryLabel"))
        self.binaryLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.binaryLabel)
        
        #Configuracoes da terceira linha de separacao.
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)

        #Configuracoes do label da mensagem codificada.
        self.encodedLabel = QtGui.QLabel(self.centralwidget)
        self.encodedLabel.setText(_fromUtf8(""))
        self.encodedLabel.setObjectName(_fromUtf8("encodedLabel"))
        self.encodedLabel.setWordWrap(True) #Quebra de linha automatica.
        self.verticalLayout.addWidget(self.encodedLabel)

        #Configuracoes da quarta linha de separacao.
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)

        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Comunicação De Dados", None))
        self.sendMessageButton.setText(_translate("MainWindow", "Send Message", None))
    
    def refresh_Labels(self, MainWindow):        
        string = self.messageEditor.text()
        binary_string = toBin(string) #Covertemos a string que esta na caixa de mensagens para binario.
        self.messageLabel.setText(_translate("MainWindow", string , None)) #Repetimos a mensagem no label coreto.                                                                         
        self.binaryLabel.setText(_translate("MainWindow", binary_string , None)) #Colocamos o codigo binario no label correto.

    #Quando o botão for pressionado chamamos a função para atualizar os labels.
    def button_Clicked(self, MainWindow):
        self.sendMessageButton.clicked.connect(self.refresh_Labels)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_Clicked(MainWindow) #Se o botao for pressionado.
    MainWindow.show()
    sys.exit(app.exec_())
