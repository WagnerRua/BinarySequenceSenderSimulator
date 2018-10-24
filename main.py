# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from ModeloQTDesigner import Ui_MainWindow
from pyqtgraph import PlotWidget
import sys
import _thread
from functions import *

class ApplicationWindow(QtWidgets.QMainWindow):    
    
    messageChanged = pyqtSignal()
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.message = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonMessage.clicked.connect(self.refreshLabelsAfterSendMessage)

    def setMessage(self, value):
        self.message = value
        self.messageChanged.connect(self.refreshLabelsAfterReceivedMessage)
        self.messageChanged.emit()

    def refreshLabelsAfterReceivedMessage(self):
        if self.message != None:
            _translate = QtCore.QCoreApplication.translate
            string = self.message
            # Covertemos a string que esta na caixa de mensagens para binario.
            binary_string = toBin(string, 1)
            # Repetimos a mensagem no label coreto.
            self.ui.messageLabel.setText(_translate("MainWindow", string))
            # Colocamos o codigo binario no label correto.
            self.ui.binaryLabel.setText(_translate("MainWindow", binary_string))
            self.setGraph(string)

    def refreshLabelsAfterSendMessage(self, MainWindow):
        # Exemplo de como ver se o checkbox está ativo
        if self.ui.checkBoxNRZ.checkState() == QtCore.Qt.Checked:
            print("Checked")

        _translate = QtCore.QCoreApplication.translate
        string = self.ui.messageEditor.text()
        sendMessageSocket(string)
        # Covertemos a string que esta na caixa de mensagens para binario.
        binary_string = toBin(string, 1)
        # Repetimos a mensagem no label coreto.
        self.ui.messageLabel.setText(_translate("MainWindow", string))
        # Colocamos o codigo binario no label correto.
        self.ui.binaryLabel.setText(_translate("MainWindow", binary_string))
        self.setGraph(string)

    def setGraph(self, string_dados):

        string_dados = toBin(string_dados, 0)
        xdados = []
        ydados = []
        contador = 0
        for x in string_dados:
            #Lista de dados do eixo y
            if contador != 0 and ydados[-1] == int(x):
                contador = contador + 1
                xdados.append(contador)
                ydados.append(int(x))
            else:
                xdados.append(contador)
                contador = contador + 1
                xdados.append(contador)
                ydados.append(int(x))
                ydados.append(int(x))

        self.ui.graphicsView.clear()
        self.ui.graphicsView.plot(xdados, ydados, title="Teste", pen='g')

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    _thread.start_new_thread(serverSocketMode,(application,))
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()