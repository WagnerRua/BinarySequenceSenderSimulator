# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from PyQt5 import QtCore, QtGui, QtWidgets
from applicationMainWindow import ApplicationWindow
from functions import *
import _thread, sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    _thread.start_new_thread(serverSocketMode,(application,))
    application.show()
    sys.exit(app.exec_())