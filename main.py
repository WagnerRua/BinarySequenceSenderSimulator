# -*- coding: utf-8 -*-
# Alunos: Lucas da Silva Nolasco e Wagner R. Ulian Agostinho

from applicationWindow import *
import _thread

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    _thread.start_new_thread(serverSocketMode,(application,))
    application.show()
    sys.exit(app.exec_())