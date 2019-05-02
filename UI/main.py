import Login as lg
from Login import Ui_LOGIN
import KeyListener as kls
from threading import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time

class MainWindow(QtWidgets.QMainWindow, Ui_LOGIN):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.close()
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    Thread(target=w.show()).start()
    time.sleep(0.2)
    Thread(target=kls.keylis()).start()
    sys.exit(app.exec_())