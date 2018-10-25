# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from ModeloQTDesigner import Ui_MainWindow
import pyqtgraph as pg
from functions import *
import sys

class ApplicationWindow(QtWidgets.QMainWindow):    
    
    messageChanged = pyqtSignal()
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.message = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.graphSettings()
        self.ui.messageEditor.returnPressed.connect(self.ui.pushButtonMessage.click)
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
        _translate = QtCore.QCoreApplication.translate
        string = self.ui.messageEditor.text()
        binary_string = toBin(string, withSpace=False)
        
        # Exemplo de como ver se o checkbox está ativo
        if self.ui.checkBoxNRZ.checkState() == QtCore.Qt.Checked:
            encoded_message = binary_string
            graph_title = 'NRZ Unipolar Encoded'
        elif self.ui.checkBoxNRZ_I.checkState() == QtCore.Qt.Checked:
            encoded_message = encodeNRZInvert(binary_string)
            graph_title = 'NRZ-Invert Encoded'
        elif self.ui.checkBoxNRZ_L.checkState() == QtCore.Qt.Checked:
            encoded_message = encodeNRZLevel(binary_string)
            graph_title = 'NRZ-Level Encoded'
        elif self.ui.checkBoxRZ.checkState() == QtCore.Qt.Checked:
            encoded_message = encodeRZ(binary_string)
            graph_title = 'RZ Encoded'

        # Repetimos a mensagem no label coreto.
        self.ui.messageLabel.setText(_translate("MainWindow", string))
        # Colocamos o codigo binario no label correto.
        self.ui.binaryLabel.setText(_translate("MainWindow", binary_string))
        # Colocamos a mesangem codificada no label correto.
        self.ui.encodedLabel.setText(_translate("MainWindow", ''.join(encoded_message) ))
        
        self.setGraph(encoded_message, graph_title)

    def setGraph(self, encoded_message, graph_title):

        xdados = []
        ydados = []
        contador = 0
        for x in encoded_message:
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

        pen = pg.mkPen('g', width=4)
        self.ui.graphicsView.clear()
        self.ui.graphicsView.setTitle(graph_title, color=(0, 0, 0))
        self.ui.graphicsView.plot(xdados, ydados, pen=pen)
        
    def graphSettings(self):

        axis_pen = pg.mkPen(color=(0, 0, 0), width=1, style=QtCore.Qt.DashLine)
        self.ui.graphicsView.setBackground('w')
        self.ui.graphicsView.getAxis('left').setPen(color=(0, 0, 0)) 
        self.ui.graphicsView.getAxis('left').setTickSpacing(100, 0.5)
        self.ui.graphicsView.getAxis('left').setPen(axis_pen)
        self.ui.graphicsView.getAxis('left').setStyle(tickTextHeight=10)
        self.ui.graphicsView.getAxis('bottom').setPen(color=(0, 0, 0))
        self.ui.graphicsView.getAxis('bottom').setTickSpacing(100, 1)
        self.ui.graphicsView.getAxis('bottom').setPen(axis_pen)
        self.ui.graphicsView.showGrid(x=True, y=True, alpha=1)
        self.ui.graphicsView.getViewBox().border = pg.mkPen(color=(0, 0, 0), width=2)
        self.ui.graphicsView.setTitle('Encoded Graphs', color=(0, 0, 0))