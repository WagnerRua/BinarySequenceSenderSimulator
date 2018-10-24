# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from ModeloQTDesigner import Ui_MainWindow
from pyqtgraph import PlotWidget
import sys, socket
import _thread

class ApplicationWindow(QtWidgets.QMainWindow):    
    
    messageChanged = pyqtSignal()
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        _thread.start_new_thread(self.serverSocketMode,())

        self.message = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonMessage.clicked.connect(self.refresh_Labels)


    def setMessage(self, value):
        self.message = value
        self.messageChanged.connect(self.refreshLabelTest)
        self.messageChanged.emit()

    def refreshLabelTest(self):
        if self.message != None:
            _translate = QtCore.QCoreApplication.translate
            string = self.message
            # Covertemos a string que esta na caixa de mensagens para binario.
            binary_string = self.toBin(string, 1)
            # Repetimos a mensagem no label coreto.
            self.ui.messageLabel.setText(_translate("MainWindow", string))
            # Colocamos o codigo binario no label correto.
            self.ui.binaryLabel.setText(_translate("MainWindow", binary_string))
            self.setGraph(string)

    def refresh_Labels(self, MainWindow):
        # Exemplo de como ver se o checkbox está ativo
        if self.ui.checkBoxNRZ.checkState() == QtCore.Qt.Checked:
            print("Checked")

        _translate = QtCore.QCoreApplication.translate
        string = self.ui.messageEditor.text()
        # Covertemos a string que esta na caixa de mensagens para binario.
        binary_string = self.toBin(string, 1)
        # Repetimos a mensagem no label coreto.
        self.ui.messageLabel.setText(_translate("MainWindow", string))
        # Colocamos o codigo binario no label correto.
        self.ui.binaryLabel.setText(_translate("MainWindow", binary_string))
        self.setGraph(string)

    # Funcao que converte strings para uma string de numeros binarios.
    def toBin(self, st, withSpace):
        string = ''
        #Coloca um espaco no final de cada conjunto de bits que correponde a uma letra
        if withSpace == 1:
            for x in st:
                string += format(ord(x), 'b') + " "
        #Sem espaco no final, usado para gerar o gráfico
        elif withSpace == 0:
            for x in st:
                string += format(ord(x), 'b')

        return string

    def setGraph(self, string_dados):

        string_dados = self.toBin(string_dados, 0)
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

    def serverSocketMode(self):
        ip = 'localhost'
        port = 65000
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind( (ip, port) )
        server.listen(1)
        while True:
            connection, client = server.accept()
            msg = connection.recv(1024)
            self.setMessage(msg.decode("utf-8"))
        
    
def main():
    message = [None]
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.message = message
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()