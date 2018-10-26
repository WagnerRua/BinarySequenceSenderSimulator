# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QLabel
from PyQt5.QtCore import pyqtSignal
from mainWindow import Ui_MainWindow
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
        self.ui.messageEditBox.returnPressed.connect(self.ui.sendMessageButton.click)
        self.ui.sendMessageButton.clicked.connect(self.refreshSendMessagePage)

    def setMessage(self, value):
        self.message = value
        self.messageChanged.connect(self.refreshReceiveMessagePage)
        self.messageChanged.emit()

    def refreshReceiveMessagePage(self):
        if self.message != None:
            _translate = QtCore.QCoreApplication.translate
            string = self.message
            # Covertemos a string que esta na caixa de mensagens para binario.
            binary_string = toBin(string, 0)
            # Repetimos a mensagem no label coreto.
            self.ui.showMessageLabel1.setText(_translate("MainWindow", string))
            # Colocamos o codigo binario no label correto.
            self.ui.showBinaryLabel1.setText(_translate("MainWindow", binary_string))
            self.setGraphReceiveMessagePage(binary_string,'teste')

    def refreshSendMessagePage(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        string = self.ui.messageEditBox.text()
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
        self.ui.showMessageLabel0.setText(_translate("MainWindow", string))
        # Colocamos o codigo binario no label correto.
        self.ui.showBinaryLabel0.setText(_translate("MainWindow", binary_string))
        # Colocamos a mesangem codificada no label correto.
        self.ui.showEncodedLabel0.setText(_translate("MainWindow", ''.join(encoded_message) ))
        
        self.setGraphSendMessagePage(encoded_message, graph_title)

    def setGraphSendMessagePage(self, encoded_message, graph_title):

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
        
    def setGraphReceiveMessagePage(self, encoded_message, graph_title):

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
        self.ui.graphicsView1.clear()
        self.ui.graphicsView1.setTitle(graph_title, color=(0, 0, 0))
        self.ui.graphicsView1.plot(xdados, ydados, pen=pen)

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
        self.ui.graphicsView.getViewBox().setYRange(-3.5,3.5)
        self.ui.graphicsView.getViewBox().border = pg.mkPen(color=(0, 0, 0), width=2)
        self.ui.graphicsView.setTitle('Encoded Graphs', color=(0, 0, 0))

        self.ui.graphicsView1.setBackground('w')
        self.ui.graphicsView1.getAxis('left').setPen(color=(0, 0, 0)) 
        self.ui.graphicsView1.getAxis('left').setTickSpacing(100, 0.5)
        self.ui.graphicsView1.getAxis('left').setPen(axis_pen)
        self.ui.graphicsView1.getAxis('left').setStyle(tickTextHeight=10)
        self.ui.graphicsView1.getAxis('bottom').setPen(color=(0, 0, 0))
        self.ui.graphicsView1.getAxis('bottom').setTickSpacing(100, 1)
        self.ui.graphicsView1.getAxis('bottom').setPen(axis_pen)
        self.ui.graphicsView1.showGrid(x=True, y=True, alpha=1)
        self.ui.graphicsView1.getViewBox().setYRange(-3.5,3.5)
        self.ui.graphicsView1.getViewBox().border = pg.mkPen(color=(0, 0, 0), width=2)
        self.ui.graphicsView1.setTitle('Encoded Graphs', color=(0, 0, 0))